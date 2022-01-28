const fs = require('fs');

const pattern = /man/gim;
const filename = 'data.txt';
var str = fs.readFileSync(filename).toString();
var myarray = str.match(pattern);
var len = myarray.length;
console.log('Occurences of pattern in the string is: ' + len);
