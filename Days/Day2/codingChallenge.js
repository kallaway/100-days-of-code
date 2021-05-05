/* Find Numbers with Even Number of Digits */
var findNumbers = function(nums) {
    var counter = 0;
    for(var i = 0; i < nums.length; i++){
        var eachElementLength = `${nums[i]}`.split('').length
        if(eachElementElement % 2 === 0){
            counter++;
        }
    }
    return counter;
};

nums = [555,901,482,1771];
console.log(findNumbers(nums));

/* Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. */
var sortedSquares = function(nums) {
    var cache = []
    for(var i = 0; i < nums.length; i++){
        cache.push(nums[i]*nums[i])
    }
    cache.sort(function(a, b) {
        return a - b;
    });
    return cache;
};

nums = [-7,-3,2,3,11];
console.log(sortedSquares(nums))