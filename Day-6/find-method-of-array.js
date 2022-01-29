var arr = [2, 4, 6, 8, 10];
var arr1 = [2, 3, 4, 7, 8];

function odd(value) {
  return (value % 2) == 1;
}

var out = arr.find(odd);
var out1 = arr1.find(odd);

console.log("Output of an array 1: " + out);
console.log("Output of an array 2: " + out1);
