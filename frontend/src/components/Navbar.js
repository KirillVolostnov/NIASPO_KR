import React from 'react';

const Navbar = () => {
    return (
        <nav>
            <h1>Туристическая Платформа</h1>
            <ul>
                <li><a href="/">Главная</a></li>
                <li><a href="/about">О нас</a></li>
                <li><a href="/booking">Бронирование</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;
