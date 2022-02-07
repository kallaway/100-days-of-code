var fs = require('fs');

var date1 = new Date();
var time_start = date1.getTime();

console.log('{Check Point} starting at: ' + time_start);
console.log("Let's start reading file");

var filename = 'output.txt';

fs.readFile(filename, (err, data) => {
  if(err)
    throw err;

  console.log("Content: " + data);
})

var date2 = new Date();
var time_end = date2.getTime();

console.log("{Check point 2} finishing at: " + time_end);
var exection_time = time_end - time_start;

console.log("Time for execution : " + exection_time);
console.log("Another task to be executed");
