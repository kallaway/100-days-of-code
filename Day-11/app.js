var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Simple Example of routes!');
})

app.get('/signup', function (req, res) {
  res.send('This is demo route for sign up');
})

app.get('/signin', function (req, res) {
  res.send('This is demo route for sign in');
})

app.get('/signin/dashboard', function (req, res) {
  res.send('this is demo for user who signed in and now reaches their dashboard');
})

app.listen(3000, function() {
  console.log('Server is listening at 3000');
})
