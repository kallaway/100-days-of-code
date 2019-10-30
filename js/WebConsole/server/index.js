const cors = require('cors');
const exec = require('child_process').execSync;
const express = require('express');
const path = require('path');

function execute(req, res) {
  console.log(req.query["cmd"]);
  try {
    const proc = exec(req.query["cmd"]);
    console.log(proc.toString());
    return res.send(proc.toString());
  } catch (error) {
    console.log("An error occurred");
    console.log(error);

    return res.send("Aww");
  }
}

const app = express();

app.use(cors());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/exec/', execute);

app.listen(5000, () =>
  console.log(`Listening on port 5000.`),
);