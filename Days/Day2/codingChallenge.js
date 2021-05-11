/* Find Duplicate Zeros */
var duplicateZeros = function(arr) {
    for(var i = 0; i < arr.length; i++){
        if(arr[i] === 0){
            arr.splice(i+1, 0, '0')
            arr.pop();
        }
    }
};

var arr = [1,0,2,3,0,4,5,0]
console.log(duplicateZeros(arr))

/* Merge Sorted Array */
var merge = function(nums1, m, nums2, n) {
    for (var i = 0; i < n; i++) {
            nums1[i + m] = nums2[i];
    }
    nums1.sort(function(a, b) {
        return a - b;
    });
};