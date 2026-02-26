// simple Node server to serve SPA with fallback
const express = require('express');
const path = require('path');
const app = express();

const FE_DIR = path.join(__dirname, 'FE');
app.use(express.static(FE_DIR));

// catch-all route serves index.html for client-side routing
app.get('*', (req, res) => {
  res.sendFile(path.join(FE_DIR, 'index.html'));
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`SPA server running on http://localhost:${port}`));
