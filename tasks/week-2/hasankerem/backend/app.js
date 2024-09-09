const express = require('express');
const cors = require('cors');  // Import the cors middleware
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Enable CORS for all routes
app.use(cors());

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// In-memory database (just an array for simplicity)
let messages = [
    { id: 1, text: 'Hello from the backend!' },
    { id: 2, text: 'Another message from the backend!' }
];

// GET route to fetch all messages
app.get('/api/messages', (req, res) => {
    res.json(messages);
});

// GET route to fetch a specific message by ID
app.get('/api/messages/:id', (req, res) => {
    const messageId = parseInt(req.params.id, 10);
    const message = messages.find(msg => msg.id === messageId);
    if (message) {
        res.json(message);
    } else {
        res.status(404).json({ error: 'Message not found' });
    }
});

// POST route to add a new message
app.post('/api/messages', (req, res) => {
    const newMessage = {
        id: messages.length + 1,
        text: req.body.text
    };
    messages.push(newMessage);
    res.status(201).json(newMessage);
});

// DELETE route to delete a message by ID
app.delete('/api/messages/:id', (req, res) => {
    const messageId = parseInt(req.params.id, 10);
    const messageIndex = messages.findIndex(msg => msg.id === messageId);
    if (messageIndex !== -1) {
        messages.splice(messageIndex, 1);
        res.status(204).send();
    } else {
        res.status(404).json({ error: 'Message not found' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Backend is running on http://localhost:${port}`);
});
