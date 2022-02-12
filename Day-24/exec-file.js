var ef = require('child_process').execFile;

var child = ef('node', ['--version'], (err, stdout, stderr) => {
  if(err){
    console.log('stderr', stderr);
    throw err;
  }
  console.log('Node.js version : ' , stdout);
})
