const fs = require('fs');

function nSCallback(error, data) {
  if (error){
    console.error('Error : ', error);
    return 
  }
  console.log(data);
}

fs.readFile('data.txt', nSCallback);
fs.readFile('file_does_not_exist.txt', nSCallback);
