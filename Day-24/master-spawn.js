var cp = require('child_process');

for (var i = 1; i < 6; i++) {
  var worker = cp.spawn('node', ['slave.js', i]);

  worker.stdout.on('data', function (data) {
    console.log('Value of Stdout : ' + data);
  });

  worker.stderr.on('data', function(data) {
    console.log('stderr: ' + data);
  });

  worker.on('close', function(code) {
    console.log('child process exited with code ' + code);
  });
}
