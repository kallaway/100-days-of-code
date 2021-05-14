/*
1) How to find the maximum occurring character in a given String? (solution)
Write an efficient Java/C/Python program to return the maximum occurring character in the input string, e.g., if the input string is "Java" then the function should return 'a'.


Read more: https://www.java67.com/2018/04/21-string-programming-and-coding-interview-questions-answers.html#ixzz6urbNxj2u

Link:  https://www.java67.com/2018/04/21-string-programming-and-coding-interview-questions-answers.html
*/

var getMaxOccuringChar = function(str) {
    var key = {};
    for(var i = 0; i < str.length; i++){
        if(!key[str[i]]){
            key[str[i]] = 1;
        } else {
            key[str[i]]++;
        }
    }
    var cache = Object.keys(key).reduce((a, b) => key[a] > key[b] ? a : b)
    if(key[cache] === 1){
        return 'none'
    } else {
        return cache;
    }
};

 str = 'mahdi'
 console.log(getMaxOccuringChar(str))

//check this and ensure time and space complexity is optimal

