/* Find Duplicate Zeros */
var duplicateZeros = function(arr) {
    for(var i = 0; i <  arr.length; i++){
        if(arr[i] === 0){
            arr.push(null)
        }
    }
    return arr;
};

var arr = [1,0,2,3,0,4,5,0]
console.log(duplicateZeros(arr))