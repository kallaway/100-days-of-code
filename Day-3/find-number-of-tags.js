var fs = require('fs');
var filename = 'data.html';
var str = fs.readFileSync(filename).toString();
var pattern = /<(\"[^\"]*\"|'[^']*'|[^'\">])*>/gim;
var myarray = str.match(pattern);
var len = myarray.length;
console.log('Occurences of pattern in the string is : ' + len);
