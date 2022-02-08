function hello(){
  console.log('This will run immediately');
}

console.log('It will Print the data immediately');

setImmediate(hello);
