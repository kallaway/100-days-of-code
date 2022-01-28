var args = process.argv.slice(2);

if (args < 1) {
  console.log('Please give email address you want to check');
  return
}

var email = args[0];
var pattern = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
var result = email.match(pattern);

if (result) {
  console.log('Valid email address');
} else {
  console.log("Please enter a valid email address");
}


