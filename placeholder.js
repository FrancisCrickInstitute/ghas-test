const mysql = require('mysql');
const express = require('express');
const app = express();

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'test'
});

app.get('/search', function (req, res) {
  const term = req.query.term;
  // 🚨 Vulnerable: SQL injection via unsanitized input
  connection.query("SELECT * FROM products WHERE name = '" + term + "'", function (err, results) {
    if (err) throw err;
    res.send(results);
  });
});

app.listen(3000);
