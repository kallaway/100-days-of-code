var assert = require('assert');

function demo(x, y, z) {
  var value = x + y + z;
  return value;
}


var output = demo(4, 1, 10);
console.log("Output : " + output);

var expected_output = 15;
console.log("Expected output: " + expected_output);

assert( output === expected_output, 'Test case is true, so this is not printed.')

