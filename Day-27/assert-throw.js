var assert = require('assert');
assert.throws(() => {
  throw new Error('Wrong value');
},
Error);
