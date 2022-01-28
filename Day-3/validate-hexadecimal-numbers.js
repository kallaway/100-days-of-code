var args = process.argv.slice(2);

if (args.length < 1) {
  console.log('Please give the Hexadecimal to validate');
  return
}
var input = args[0];
var pattern = /^[a-fA-F0-9]+$/g;

var result = input.match(pattern);

if (result) {
  console.log('Valid Hexadecimal Number');
} else {
  console.log('Not Valid Hexadecimal Number');
}
