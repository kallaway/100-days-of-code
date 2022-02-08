function hello(){
  console.log('This will run recursively');
}

console.log('It will Print the data recursively after a delay of 2000ms again and again');

setInterval(hello, 2000);
