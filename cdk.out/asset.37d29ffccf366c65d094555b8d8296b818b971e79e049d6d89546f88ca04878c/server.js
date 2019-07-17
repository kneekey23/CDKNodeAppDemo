'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.use(express.static(__dirname + '/public'));
app.get('/', (req, res) => {
  //res.send('Hello world\n');
  res.sendFile('index.html', { root: __dirname });
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);