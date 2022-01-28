// password must contain 1 capital letter
// password must contain 1 small letter
// password must contain 1 number
// password must contain 1 special character
// password length must be within in the range [6,16]

var args = process.argv.slice(2);

if (args.length < 1) {
  console.log('Please give the password to validate');
  return
}

var input = args[0];
var pattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;;

var result = input.match(pattern);

if (result) {
  console.log('Valid Password');
} else {
  console.log('Not Valid Password');
}
