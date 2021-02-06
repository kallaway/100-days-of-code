const cors = require('cors');
const exec = require('child_process').execSync;
const express = require('express');
const fs = require('fs');
const multer = require("multer");
const path = require('path');

const handleError = (err, res) => {
  res
    .status(500)
    .contentType("text/plain")
    .end("Something went wrong!");
};

const upload = multer({
  dest: "tmp"
  // you might also want to set some limits: https://github.com/expressjs/multer#limits
});

function saveImage(req, res) {
  const tempPath = req.file.path;
  const extension = req.file.extension;
  const randomNumber = Math.random();
  const targetPath = path.join(__dirname, "./uploads/image" + randomNumber + path.extname(
    req.file.originalname).toLowerCase());
  
  try {
    fs.renameSync(tempPath, targetPath);
    const proc = exec("./basic_ocr uploads/image" + randomNumber + path.extname(
      req.file.originalname).toLowerCase());

    fs.unlinkSync(targetPath);
    
    console.log(proc.toString());

    return res.send(proc.toString());
  } catch (error) {
    return handleError(err, res);
  }
}

const app = express();

app.use(cors());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/static/js/2.ff727787.chunk.js', (req, res) => {
  res.sendFile(path.join(__dirname + '/static/js/2.ff727787.chunk.js'));
});

app.get('/static/js/main.b339802c.chunk.js', (req, res) => {
  res.sendFile(path.join(__dirname + '/static/js/main.b339802c.chunk.js'));
});

app.get('/static/css/main.c19c5f7a.chunk.css', (req, res) => {
  res.sendFile(path.join(__dirname + '/static/css/main.c19c5f7a.chunk.css'));
});

app.post(
  "/upload",
  upload.single("image" /* name attribute of <file> element in your form */),
  saveImage
);

app.listen(5000, () =>
    console.log(`Listening on port 5000.`),
);