var assert = require('assert');

assert.ok(true, "No Error");

assert.ok(1, "No Error");

assert.ok(false, "It is an Error");

assert.ok(0, "Again Error");

var a = 10;

var b = 20;

assert(a > b, "A should be greater than B"); 
