import React, { useState } from 'react';

const BookingForm = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [date, setDate] = useState('');
    const [country, setCountry] = useState('');
    const [city, setCity] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('/api/bookings', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, date, country, city })
        });
        if (response.ok) {
            alert('Бронирование успешно!');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Имя" value={name} onChange={(e) => setName(e.target.value)} required />
            <input type="email" placeholder="Эл. почта" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
            <input type="text" placeholder="Страна" value={country} onChange={(e) => setCountry(e.target.value)} required />
            <input type="text" placeholder="Город" value={city} onChange={(e) => setCity(e.target.value)} required />
            <button type="submit">Забронировать</button>
        </form>
    );
};

export default BookingForm;
