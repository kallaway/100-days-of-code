var assert = require('assert');

function demo(x, y, z) {
  var value = x + y + z;
  return value;
}


var output = demo(3, 2, 10);
console.log("Output : " + output);

var expected_output = 12;
console.log("Expected output: " + expected_output);

assert( output === expected_output, 'This is not what we expected')

