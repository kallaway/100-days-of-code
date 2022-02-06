var zlib = require('zlib');

var fs = require('fs');

var zip = zlib.createGzip();

var read = fs.createReadStream('newfile.txt');

var write = fs.createWriteStream('newfile.txt.gz');

read.pipe(zip).pipe(write);

console.log("Zipped successfully");
