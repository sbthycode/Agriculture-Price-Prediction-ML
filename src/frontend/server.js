// server.js
const express = require('express');
const path = require('path');

const app = express();
const port = 3000; // Choose a port number

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'template')));

// Listen for incoming requests
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

