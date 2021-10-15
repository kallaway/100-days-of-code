// Bracket Matcher
// HIDE QUESTION
// Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

//My solution:

function BracketMatcher(str) { 

  // code goes here  
  let arr = str.split('');
  // console.log(arr);
  let left=0;
  let right=0;
  let diff =0;

  for (i=0; i< arr.length; i++){
    if (arr[i] === '(') {left ++}
    else if (arr[i] === ')') {right ++};
  }
  diff = Math.abs(left-right);
  // console.log ('diff is ', diff)
  if (diff > 0){ diff = 0}
  else if (diff === 0){diff=1};
  return diff; 

}
   
// keep this function call here 
console.log(BracketMatcher('(cod)e ) (lsakjf)'));
console.log(BracketMatcher('(cod)e  (lsakjf)'));