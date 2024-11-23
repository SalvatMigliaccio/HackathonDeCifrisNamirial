import React, { useState } from 'react';
import Textfield from '../components/Textfield';
import './Form.css';
import { Link } from 'react-router-dom';

const Register: React.FC = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        // Handle registration logic here
        console.log('Username:', username);
        console.log('Email:', email);
        console.log('Password:', password);
    };

    return (
        <div className="form-container">
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <Textfield
                    label="Username"
                    type='text'
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
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
                <button type="submit">Register</button>
                <p>
                    Already have an account? <Link to="/login">Log in</Link>
                </p>
            </form>
        </div>
    );
};

export default Register;