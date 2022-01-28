const fs = require('fs');

function nSCallback(error, data) {
  if (error){
    console.error('Error : ', error);
    return 
  }
  console.log(data);
}
try {
  fs.readFile('file_does_not_exist.txt', (err, data) => {
    if (err)
      throw err;
    console.log(data);
  });
} catch(err) {
  console.log(err);
}


