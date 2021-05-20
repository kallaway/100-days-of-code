/*

var fullJustify = function(words, maxWidth) {
    //iterate through elements in the array
        //add length to counter and keep adding until its less than maxWidth including width
        //add to string var and push to array

    for(var i = 0; i < words.length; i++){
        var counter = 0;
        if(counter <= maxWidth){
            var cache = '';
            counter + words[i].length;
            cache += words[i]
        }
    }
};

var words = ["This", "is", "an", "example", "of", "text", "justification."];
var maxWidth = 16;
console.log(fullJustify(words, maxWidth))

*/

function hasDuplicates(array) {
    return (new Set(array)).size !== array.length;
}

var lengthOfLongestSubstring = function(s) {
    var str = s.split('');
    var cache = [];
    var count = [];
    if(s.length === 0){
        return 0;
    }
    for(var i = 0; i < str.length; i++){
        cache.push(str[i]);
        if(hasDuplicates(cache) === false){
            console.log(cache)
            console.log(cache.length)
            count.push(cache.length)
            console.log(count)
        } else {
            cache = [];
        }
    }
    return Math.max(...count)
};

var s = 'aab';
console.log(lengthOfLongestSubstring(s))