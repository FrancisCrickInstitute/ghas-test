const express = require('express');
const app = express();
const db = require('some-db-lib');

app.get('/users', function (req, res) {
  const user = req.query.name;
  // InsecureSQL injection vulnerability
  db.query("SELECT * FROM users WHERE name = '" + user + "'", function (err, result) {
    if (err) throw err;
    res.send(result);
  });
});

app.listen(3000);
