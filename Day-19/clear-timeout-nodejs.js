function hello(){
  console.log('This will not run at all');
}

console.log('It is supposed to print the data immediately');
var imm = setImmediate(hello);
clearImmediate(imm);
