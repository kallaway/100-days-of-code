var assert = require('assert');

var a = 10;
var b = '10';
var c = 10;

assert.strictEqual(a, c, "Nothing printed");
assert.strictEqual(a, b, "Err acc to strict equality comparison");


