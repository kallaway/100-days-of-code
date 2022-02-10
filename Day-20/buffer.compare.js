var buff1 = Buffer.from('Khangaikhuu');
var buff2 = Buffer.from('Khangaikhuu');
var output = buff1.compare(buff2);
console.log(output);

if (output < 0) {
  console.log(buff1 + " comes from " + buff2);
} else if (output == 0) {
  console.log(buff1 + " is same as " + buff2);
} else {
  console.log(output + " comes after " + buff2);
}
