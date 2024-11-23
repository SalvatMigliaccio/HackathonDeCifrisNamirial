import React, { useState } from 'react';
import Textfield from '../components/Textfield';
import './Form.css';
import { Link } from 'react-router-dom';
import auth from '../services/auth';

const Login: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        auth.login(email, password)
        
    };

    return (
        <div className="form-container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                    
            <Textfield
                label="Email"
                type='email'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <Textfield
                label="Password"
                type='password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
                <button type="submit">Login</button>
                <p>
                    Don't have an account? <Link to="/register">Register</Link>
                </p>
            </form>
        </div>
    );
};

export default Login;