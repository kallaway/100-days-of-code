var assert = require('assert');

var a = 10;
var b = '10';
var c = 10;


assert.notDeepStrictEqual(a, b, "Nothing printed because they are using == for comparison");

assert.notDeepStrictEqual(a, c, "Error because values does not match");


