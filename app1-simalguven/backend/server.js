const express = require('express');
const app = express();
const port = 3000;

// Serve the frontend files
app.use(express.static('public'));

// API endpoint
app.get('/api/message', (req, res) => {
    res.json({ message: 'Hello from the Backend!' });
});

// Start the server
app.listen(port, () => {
    console.log(`Backend server running on port ${port}`);
});


