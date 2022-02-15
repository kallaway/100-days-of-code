var assert = require('assert');

var a = 50;
var b = '50';
var c = 50.25;


assert.equal(a, b, "Nothing printed because they are using == for comparison");

assert.equal(a, c, "Error because values does not match");


