function hello(){
  console.log('This will not run at all');
}

console.log('It is supposed to Print the data recursively after a delay of 2000 ms again and again');
var s_int = setInterval(hello, 2000);
clearInterval(s_int);
