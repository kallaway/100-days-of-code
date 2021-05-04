/* Find Max Consecutive Ones in a Given Array*/
var findMaxConsecutiveOnes = function(nums) {
    var cache = [];
    var counter = 0;
    for(var i =0; i <= nums.length;i++){
        if(nums[i] === 1){
            counter++;
        } else {
            cache.push(counter);
            counter = 0;
        }
    }
    return Math.max(...cache);
};

nums = [1,0,1,1,0,1,1,1]
console.log(findMaxConsecutiveOnes(nums))
