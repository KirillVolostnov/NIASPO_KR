from flask import Flask, jsonify, request
import psycopg2
import redis

app = Flask(__name__)

# PostgreSQL connection
conn = psycopg2.connect(
    host="db",
    database="tourism",
    user="user",
    password="password"
)

# Redis connection
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

with conn.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            date DATE NOT NULL,
            country VARCHAR(100),
            city VARCHAR(100)
        );
    """)
    conn.commit()


@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bookings;")
        bookings = cursor.fetchall()
        bookings_list = [
            {'id': booking[0], 'name': booking[1], 'email': booking[2], 'date': booking[3], 'country': booking[4], 'city': booking[5]}
            for booking in bookings
        ]
    return jsonify(bookings_list)

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.json
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO bookings (name, email, date, country, city) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
                (data['name'], data['email'], data['date'], data['country'], data['city'])
            )
            booking_id = cursor.fetchone()[0]
            conn.commit()

            redis_client.hmset(f"booking:{booking_id}", {
                'id': booking_id,
                'name': data['name'],
                'email': data['email'],
                'date': data['date'],
                'country': data['country'],
                'city': data['city']
            })

        return jsonify({'id': booking_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cache', methods=['GET'])
def get_cache():
    return jsonify(redis_client.get('cache_key') or "No cache")

@app.route('/api/cache', methods=['POST'])
def set_cache():
    data = request.json
    redis_client.set('cache_key', data['value'])
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
