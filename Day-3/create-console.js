var ws = require('fs');

const {Console} = require('console');

const output = ws.createWriteStream('./stdout.log');
const errOutput = ws.createWriteStream('./stderr.log');

const print = new Console(output, errOutput);
const roll = 839147;

print.log('roll: %d', roll); 
print.log('This will be stored in a file'); 
