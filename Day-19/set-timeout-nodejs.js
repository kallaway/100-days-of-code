function hello(){
  console.log('This will run only once');
}

console.log('It will Print the data once after a delay of 2000ms');

setTimeout(hello, 2000);
