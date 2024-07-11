import React, { useState, useEffect } from 'react';
import Login from './Login';
import Home from './Home';

const App = () => {
    const [token, setToken] = useState(localStorage.getItem('token'));

    useEffect(() => {
        localStorage.setItem('token', token);
    }, [token]);

    const logout = () => {
        setToken('');
        localStorage.removeItem('token');
    };

    return (
        <div>
            {token ? <Home logout={logout} /> : <Login setToken={setToken} />}
        </div>
    );
};

export default App;
