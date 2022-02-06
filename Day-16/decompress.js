var zlib = require('zlib');

var fs = require('fs');

var unzip = zlib.createUnzip();

var read = fs.createReadStream('newfile.txt.gz');

var write = fs.createWriteStream('unzip.txt');

read.pipe(unzip).pipe(write);

console.log("Unzipped successfully");
