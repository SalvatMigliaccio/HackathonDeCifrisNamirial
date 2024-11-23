import React, { useState } from 'react';
import { Typography, Tabs, Tab, Box, List, ListItem, ListItemText } from '@material-ui/core';
import Navbar from '../components/navbar';
import './Dashboard.css';
import Textfield from '../components/Textfield';

const Dashboard: React.FC = () => {
    const [selectedTab, setSelectedTab] = useState(0);
    const [selectedPractice, setSelectedPractice] = useState<number | null>(null);

    const user = {
        id: 1,
        email: 'amz@bit4id.com',
        name: 'Andrea',
        isOperator: false
    }

    const practices = [
        { id: 1, name: 'Richiesta Carta identità', steps: ['Step 1', 'Step 2', 'Step 3'] },
        { id: 2, name: 'Pagamento mora spazzatura', steps: ['Step A', 'Step B'] },
        { id: 3, name: 'ottenimento condono edilizio', steps: ['Step X', 'Step Y', 'Step Z'] },
    ];

    const closedPractices = [
        { id: 4, name: 'Richiesta di sovvenzione', steps: ['Step 1', 'Step 2', 'Step 3'] },
        { id: 5, name: 'Pagamento tasse', steps: ['Step A', 'Step B'] },
        { id: 6, name: 'ottenimento permesso di soggiorno', steps: ['Step X', 'Step Y', 'Step Z'] },
    ];


    const handleTabChange = (_event: React.ChangeEvent<{}>, newValue: number) => {
        setSelectedTab(newValue);
        console.log('Selected tab:', newValue);
        setSelectedPractice(null);
    };

    const handlePracticeClick = (practiceId: number) => {
        setSelectedPractice(practiceId);
    };

    return (
        <div style={
            { display: 'flex', flexDirection: 'column', height: '100vh', width: '80vw' }
        }>
            <Navbar />
            <Tabs value={selectedTab} onChange={handleTabChange} centered>
                {
                    !user.isOperator ? [
                        <Tab label="Pratiche aperte" />,
                        <Tab label="Pratiche chiuse" />] : [
                        <Tab label="Avvia Pratica" />,
                        <Tab label="Firma step" />,]
                }
            </Tabs>
            <>
                {
                    !user.isOperator ? (<Box p={3} className='tabBox'>
                        {selectedTab === 0 && (
                            <List className='sinistra'>
                                {practices.map((practice) => (
                                    <ListItem button key={practice.id} onClick={() => handlePracticeClick(practice.id)}>
                                        <ListItemText primary={practice.name} />
                                    </ListItem>
                                ))}
                            </List>
                        )}
                        {selectedTab === 1 && (
                            <List className='sinistra'>
                                {closedPractices.map((practice) => (
                                    <ListItem button key={practice.id} onClick={() => handlePracticeClick(practice.id)}>
                                        <ListItemText primary={practice.name} />
                                    </ListItem>
                                ))}
                            </List>
                        )}
                        {selectedPractice !== null && (
                            <Box
                                style={{ marginTop: '20px', flex: 2, width: '100%' }}>
                                <Typography variant="h6">Steps for Practice {selectedPractice}</Typography>
                                <List>
                                    {practices.find((practice) => practice.id === selectedPractice)?.steps.map((step, index) => (
                                        <ListItem key={index}>
                                            <ListItemText primary={step} />
                                        </ListItem>
                                    ))}
                                </List>
                            </Box>
                        )}</Box>
                    ) : (<>

                        {selectedTab === 0 && (<div>
                            <Typography variant="h6" style={{ marginTop: '20px'}}>Start a new practice</Typography>
                            <form style={
                                { display: 'flex', flexDirection: 'column', width: '50%',
                                    alignContent: 'center', margin: 'auto', gap: '20px'
                                 }
                            } >
                                <Textfield label="Practice name" type='text' 
                                    value = {''}
                                    onChange = {() => {}}
                                />
                                <Textfield label="User's email" type='text' 
                                    value = {''}
                                    onChange = {() => {}}
                                />
                                <button type="submit">Start</button>
                            </form></div>
                        )}
                        {
                            selectedTab === 1 && (
                                <Box p={3} className='tabBox'>
                                    <List className='sinistra'>
                                        {practices.map((practice) => (
                                            <ListItem button key={practice.id} onClick={() => handlePracticeClick(practice.id)}>
                                                <ListItemText primary={practice.name} />
                                            </ListItem>
                                        ))}
                                    </List>{selectedPractice !== null &&
                                        <Box
                                            style={{ marginTop: '20px', flex: 2, width: '100%' }}>
                                            <Typography variant="h6">Sign your practice step</Typography>
                                            <button type="submit">Sign</button>
                                        </Box>}
                                </Box>
                            )
                        }

                    </>
                    )
                }
            </>
        </div>
    );
};

export default Dashboard;