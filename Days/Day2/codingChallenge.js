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