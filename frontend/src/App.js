import React from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import About from './pages/About';
import Booking from './pages/Booking';

const App = () => {
    return (
        <div>
            <Navbar />
            <Home />
            <About />
            <Booking />
            <Footer />
        </div>
    );
};

export default App;
