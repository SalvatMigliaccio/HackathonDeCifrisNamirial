import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@material-ui/core';
import { IoMdExit } from "react-icons/io";


const Navbar: React.FC = () => {
    const handleLogout = () => {
        // Implement logout functionality here
        console.log('Logout clicked');
    };

    return (
        <AppBar position="static" elevation={0} style={{
            borderBottom: '1px solid #e0e0e0',
            backgroundColor: 'transparent'
        }}>
        <Toolbar style={{ display: 'flex', justifyContent: 'space-between' }}>
            <div style={{ flex: 1 }}></div>
            <Typography variant="h6" style={{ flex: 1, textAlign: 'center' }}>
                <span style={{ color: '#00B050' }}>XRP</span> <br/>
                e<span style={{ color: '#00B050' }}>X</span>tended 
                <span style={{ color: '#00B050' }}>R</span>ing 
                <span style={{ color: '#00B050' }}>P</span>rivacy

            </Typography>
            <div style={{ padding:0, flex: 1, display:'flex'
            , justifyContent:'flex-end'
             }}>
            <Button color='secondary' variant='text' onClick={handleLogout} >
                <IoMdExit size={24} />  
            </Button></div>
        </Toolbar>
        </AppBar>
    );
};

export default Navbar;