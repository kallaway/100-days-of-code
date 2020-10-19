//datatypes
"", 5, true, {}, []
//primatives are datas that Javascript will use AS IS, and don't need further eval.
//expressions need to be evaluated to primatives by JS before moving on.
console.log("5");
console.log(5+5);
console.log(5>5);
//logical operators sometimes ask a question, sometimes perform logic;
//questions > < <= >= == === != !==
// == equal value
// === equal value AND type
// != not equal value
"2" != 2 // returns false because equal value
"2" !== 2 //returns true because not same type
console.log(!{});
if(""){
    console.log("string is truthy!")
}else{
    console.log("string is falsey");
}
//"", null, undefined, false, 0, these are "falsey" values
//-5, 10, {}, [], truthy values
// !== not equal value or type
//logical operators that do something, perform logic
// || or, && and ? ternary op for "if";
// || and && ALWAYS return just one expression.
console.log("lauren"||"garelick");
// || - if left side is truthy, return left, else return right side;
// && - if left side is truthy, return right, else return left side;
console.log("hello" && null);
//play with this later
console.log(("" || (null && undefined)) || "bonus" );
//write a function that takes in a array of strings, and log BINGO if word has 4 letters or more,
//and log BONGO if word has less than 4 letters
const array = ["hello", "my", "name", "is", "drake"];
function bingo(arr){
    for (let i = 0; i < arr.length; i++) {
        if(arr[i].length>=4){
            console.log("BINGO");
        }else{
            console.log("BONGO")
        }      
    }
}
bingo(array)
//forEach vs map;
//both loop through an array, forEach doesn't return a copy of the array, map returns a shallow copy of the array, modified however you want;
//shallow copies are like photo copies, loses the reference to original object or data, etc. and only copies values on the surface level, deeper nested values are still referenced at original pointer. 
console.log(array.map(function(value){
    return value.toUpperCase()
}));
//spread operator also creates a shallow copy on the surface level, so it loses reference to the original pointer but not for deeper references;
const newArray = [...array];
array.push("lauren");
console.log(newArray);
console.log(array);
//Algorithm 1 
//write a function that takes in an array of any number of values, and return 
//an array of only non-repeating values in the array
//eg. [2,3,6,2,1,7,6] will return [3,1,7] because 2 and 6 are repeating values and shouldn't be included in the output;
//Algorithm 2
//write a function that takes in a string, and returns true if the string has an even number of vowels,
//eg. "Where is waldo?" will return false because string has 5 vowels and not an even number;
//Algorithm 3
//write a function that takes in an array of unsorted numbers, and returns an array
//of the numbers sorted from 1 to 9 on all digits.
//eg [2,335,23433,21311,12211,11,1,32124] will return [1,11,12211,2,21311,23433,32124,335];