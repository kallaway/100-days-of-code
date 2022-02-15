var assert = require('assert');

var a = 10;
var b = '10';

assert.deepStrictEqual(a, b, "Error because they are using === for comparison");


