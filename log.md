# 100 Days Of Code - Log

### Day 1: Oct. 6th, 2021

**Today's Progress**: Completed LeetCode challenge: Find All Duplicates in an Array. Code is below:
```
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {    
    const set = new Set(nums)
    
    const filter = nums.filter(item => {
        if(set.has(item)){
            set.delete(item)
        }else{
            return item
        }
    })
    return [... new Set(filter)]
};

```

**Thoughts**: One goal for myself while being stationed in Japan is to get better with coding challenges. So I plan on doing one coding challenge a day. Today when I read this particiular challenge, I immediately thought about creating a Set. A Set will return an object with only unique vaules (no repeats). Then I can filter the original array that has the repeated values, and if the set I created has that element in it, we can delete that item from the set. If the item is not in the set, then just return the item. Once that is completed we can convert our set to a new array that holds only the repeated values using the spread operator.

**Link(s) to work**:
[LeetCode](https://leetcode.com/TiaRose7/)