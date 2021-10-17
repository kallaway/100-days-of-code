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

**Thoughts**: One goal for myself while being stationed in Japan is to get better with coding challenges. So I plan on doing one coding challenge a day. Today when I read this particular  challenge, I immediately thought about creating a Set. A Set will return an object with only unique values (no repeats). Then I can filter the original array that has the repeated values, and if the set I created has that element in it, we can delete that item from the set. If the item is not in the set, then just return the item. Once that is completed we can convert our set to a new array that holds only the repeated values using the spread operator.

**Link(s) to work**:
[LeetCode](https://leetcode.com/TiaRose7/)
### Day 2: Oct. 7th, 2021

**Today's Progress**: Spent some time updating packages in one of my old projects.

**Thoughts**: I haven't touched this project in over a year and the number of critical and high vulnerabilities this project had is amazing. Wrangling with this amount of outdate packages has been good practice to ensure what it takes to get old legacy code up to speed. In my previous job we had to do something similar, so the more I practice I get, the better.

**Link(s) to work**: [Remember-Me](https://github.com/TRose2014/remember-me)

### Day 3: October 12th, 2021 

**Today's Progress**: Cleaned up remember-me repo and cleared out outdated dependencies. Also updated readme in remember-me repo. Started scaffolding out new project for button challenge

**Thoughts**: Part of being a software developer is to up keep your old code and since this remember me project is special to me I wanted to make sure it still functions. I need to work on the admin page for the remember me project but currently I want to work on a front end challenge to refresh my React.js knowledge

**Link(s) to work**: [Button Challenge Info](https://devchallenges.io/challenges/ohgVTyJCbm5OZyTB2gNY)

### Day 4: October 13th, 2021

**Today's Progress**: Added [React-bootstrap](https://react-bootstrap.github.io/components/buttons/) to button challenges project and started playing around with it.

**Thoughts**: React bootstrap allows me to use pre-built, pre-styled components such as a button. However when I try various styles they all look like the same, so will need to revisit why styling isn't there.

**Link(s) to work**: [Button Challenge Repo](https://github.com/TRose2014/button-challenge/tree/dev)

### Day 5: October 17th, 2021

**Today's Progress**: Setting up a new repo, this project will display all the snacks we try in Asia

**Thoughts**: I had an idea on creating a food items page for the family since we will be living in Asia for a bit. It will be similar to my remember me project, but I will just be using a json file to subsitute a database. This gave me a refersher on using [MUI](https://mui.com/getting-started/installation/) and mapping over data in React.

**Link(s) to work**: [Rose-travel](https://github.com/TRose2014/rose-travel)


### Template
### Day 1: 

**Today's Progress**: 

**Thoughts**: 

**Link(s) to work**:
