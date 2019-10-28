const Commands = require('commands').Commands;
const cors = require('cors');
const exec = require('child_process').execSync;
const express = require('express');
const path = require('path');

function execute(req, res) {
  try {
    const proc = exec(req.query["cmd"]);

    return res.send(proc.toString());
  } catch (error) {
    console.log("An error occurred");

    return res.send("Aww");
  }
}

function getCurrentDirectory(req, res) {
  const proc = exec(Commands.GET_CURRENT_DIRECTORY);
  return res.send(proc.toString());
}

const app = express();

app.use(cors());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/exec/', execute);

app.get('/gwd/', getCurrentDirectory);

app.listen(5000, () =>
  console.log(`Listening on port 5000.`),
);