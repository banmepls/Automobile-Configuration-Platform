// Node.js Server Configuration
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname, 'public')));

// Start server with console confirmation
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});