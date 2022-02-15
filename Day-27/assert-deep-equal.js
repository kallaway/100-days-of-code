var assert = require('assert');

var a = 10;
var b = '10';
var c = 10.25;


assert.deepEqual(a, b, "Nothing printed because they are using == for comparison");

assert.deepEqual(a, c, "Error because values does not match");


