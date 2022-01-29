var arr = [2, 4, 6, 8, 10];
var arr1 = [2, 3, 4, 6, 8];

function even(value) {
  return (value % 2) == 0;
}

var out = arr.filter(even);
var out1 = arr1.filter(even);

console.log("Output of an array 1: " + out);
console.log("Output of an array 2: " + out1);
