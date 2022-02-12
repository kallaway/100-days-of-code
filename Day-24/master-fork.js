var cp = require('child_process');

for (var i=1; i<6; i++) {
  var worker = cp.fork("slave.js", [i]);


  worker.on('close', function(code) {
    console.log('child process exited with code ' + code);
  })

}
