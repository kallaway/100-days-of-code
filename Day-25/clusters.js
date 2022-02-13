var cluster = require('cluster');
var http = require('http');

var numOfCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log('Master with Process ID : ' + process.pid + ' is running');

  for (var i=0; i < numOfCPUs; i++){
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log('worker with Process ID : ' + worker.process.pid + ' died');
  });
} else {
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end('An example of clusters\n');
  }).listen(3001);

  console.log('Worker with Process ID : ' + process.pid + ' started');
}

