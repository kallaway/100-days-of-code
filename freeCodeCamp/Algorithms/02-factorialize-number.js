// https://www.freecodecamp.org/challenges/factorialize-a-number

function factorialize(num) {
  var j = 1;
  for(var i = 2; i <= num; i++){
    if (i <= num){
      j *= i;
    }
  }
  return j;
}
factorialize(5); // 120
