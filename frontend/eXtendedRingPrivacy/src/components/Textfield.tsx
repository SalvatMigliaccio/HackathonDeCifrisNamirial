import React from 'react';
import './Textfield.css';

interface TextfieldProps {
    label: string;
    value: string;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
    type?: string;
}

const Textfield: React.FC<TextfieldProps> = ({ label, value, onChange, placeholder = '', type = 'text' }) => {
    return (
        <div className="form__group field">
            <input
            className="form__field" 
                type={type}
                value={value}
                onChange={onChange}
                placeholder={placeholder} />
            <label className="form__label">{label}</label>
        </div>

    );
};

export default Textfield;