var pivotIndex = function(nums) {
    var allButFirst = nums.slice(1, nums.length);
    var allButLast = nums.slice(0, nums.length-1)
    var reducer = (accumulator, currentValue) => accumulator + currentValue;
    if(allButFirst.reduce(reducer) === 0){
        return 0;
    }
    
    for(var i = 1; i < nums.length-1; i++){
      var left = nums.slice(0,i)
      var right = nums.slice(i+1)
      if(left.reduce(reducer) === right.reduce(reducer)){
          return i;
      }
    }
    if(allButLast.reduce(reducer) === 0){
        return nums.length-1;
    }
    return -1;
};

var nums = [1,7,3,6,5,6];
console.log(pivotIndex(nums))
 //loop through array
        //set variable index as a tracker
        //conditional:  if index is zero, sum from i+1 to end of arr
            //if summation is equal
                //if index is left edge or end 
                    //return zero   
            //else 
                //check elements from left and right is sum
                    //if true
                        //return index
    //return -1 if no such index exists

/*
I: array of numbers
O: return pivot index 
C:
E:
*/

/* RECURSION REV
function processDoll(doll){
    // 1. base case
    //if we found the piece of chocolate
        //return yum yum
    //another if states for if there are no more dolls AND no choc
        //return 'no choc here'
    // 2. recursive call to itself
    //else
        //process smaller doll
}
*/

/* FACTORIAL RECURSION EXAMPLE
//n! (3! = 3*2*1)
function factorial(n){
    //base case
    if(n === 1 || n === 0){
        return 1;
    } else {
        return n * factorial(n-1)
    }
}

console.log(factorial(4))

*/