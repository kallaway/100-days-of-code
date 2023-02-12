# 100 Days Of Code - Log

### Day 1: 4th Feb 2023
<details>
**Today's Progress**: Learnt basic Bootstrap- Card, Grid & Conditional Rendering & toggle function on md.

**Before Thoughts:** 
1. I decided to join this challenges without publicly announce it on Twitter. I'm excited. The hardest at this moment would be I doubt I will able to just do purely coding for an hour without counting together the time spent on tutorial or reading but I will try my best.  
2. First day, I decided to continue learning React that I've been doing in the last few days. Will learn:
  * Rendering lists
  * Conditional Rendering

**After Thoughts:** 
1. Used Bootsrap to style my Pokemon exercise. It's a lot harder than Tailwind in my opinion. Used Bootstrap's Card & Grid system to style. Also need to use double {} when we use style attribute in JSX. 
2. Learnt Conditional Rendering: ```if...else``` statement, Ternary Operator and Logical Operator.
3. Special note for Logical Operator, you **CANNOT** put numbers (ZERO) on the left side of &&, otherwise React will render ZERO.
The below example, will render as 0
```
const Component = () => {
const count = 0
 return (
  <>
   {count && <p>Testing!</p>}
  </>
 )
 ```
 4. Also <details> tag (+ closing tag) for [markdown toggle](https://www.reddit.com/r/ObsidianMD/comments/j1770s/heres_how_to_create_a_toggle_switch_in_markdown/).

**Link to work:** 
1. [Pokemon App - using Bootsrap to style](https://codesandbox.io/s/pokedex-forked-0toh8l?file=/src/Pokemon.jsx)
2. [React Beta - Conditional Rendering](https://beta.reactjs.org/learn/conditional-rendering)
 </details>
 
---
 
 ### Day 2: 5th Feb 2023
 <details>

**Today's Progress**: Continue with Conditional Rendering. Did a weather exercise and did some vanilla CSS styling to it. Read passing props to components but I'm still a bit confused. Will read more & watch some videos tomorrow.

**Thoughts:** 
1. I had some trouble to do the Weather Forecast exercise. Couldnt get the Switch stmt working but got it worked eventually. But still my skill is abit rusty.
2. Felt good to use vanilla CSS to style this. 1 thing I will take out from this is how to add background-image and how to make background-image not repeating and cover.
3. Read the docs on React Beta - Passing props to a Components and done 2 exercises. I still cant really understand and will read more tomorrow.

**Link to work:** 
1. [React-Weather Forecast](https://codesandbox.io/s/w7d2-weather-forecast-again-oeo0d8?file=/src/styles.css)
2. [React: Passing props to component exercise 1](https://codesandbox.io/s/react-passingprops-e1-pxeqk9)
3. [React Beta - Passing JSX as children](https://codesandbox.io/s/reactbeta-passingjsxchildren-bpulxm)
</details>

---

### Day 3: 6th Feb 2023
<details>

**Today's Progress**: I did some reading for event handlers.

**Thoughts:** 
* Normal React components are self-closing tag. But to use props.children, you need to do.. i.e. ```<Button> … </Button>```
####Event Handler
* Must be passed but not called! ```onClick={handleClick}```, not ```onClick={handleClick()}```.
* ```e.stopPropagation()``` : to stop event propagation
* ```e.preventDefault()``` : to stop some browser event default behaviors, like submit from ```<form>```

**Link to work:** 
1. [Stop Propagation & props.children example](https://codesandbox.io/s/eventhandlers-stopporpagation-42n5f2)
2. [Stop default behavior example](https://codesandbox.io/s/eventhandler-preventdefault-9c0qjn?file=/src/App.js)
</details>

---

### Day 4: 7th Feb 2023
<details>

**Today's Progress**: 
* Done some coding challenges & APIs.

**Thoughts:** 
* Not much coding today. Did 1 coding challenges, learnt "flattening an array" is to reduce the dimensionality of an array. Can use .flat() or reduce method. 
* I learnt some API today as I'm always confused about API.

**Link to work:** 
1. [Codewars-Flattening the array](https://www.codewars.com/kata/reviews/5251f603dc71afdb4f0002d5/groups/63e18ebb17b96d000140ee47)
2. [APIs for Beginner](https://www.youtube.com/watch?v=WXsD0ZgxjRw)
</details>

---

### Day 5: 8th Feb 2023
<details>

**Today's Progress**: 
* Did not do much (but still able to code for an hour!), I attended a few workshops/events today: Job Seeker workshop on cover letter, catch-up with career coach and classmates & Zendesk Woman in Tech event.
* Did some exercise on React Beta docs. Tried myself to recreate this Sculpture demo on the website to play with State. It was fun and gave me some confidence back about React! Yay!

**Thoughts:** 
* State is like a memory of a component. Components use it to remember info between rendering.
* useState Hook to declare state variables.
* Hooks are special functions in React and only available while React is rendering.
* We should not call hooks inside conditional stmt, for loop or nested functions.
* They are private and isolate to the component. If you have the same components twice in your React app, the state will not be affected by another component. (Hope you understand, if not Read the Manual!)
* If you want the state of both components to be the same, you should lift the state to the common parents. I guess I will learn this tomorrow. 
* You SHOULD NOT mutate the state!

**Link to work:** 
1. Did all my coding in this exercise - [React beta- State Exercise 1](https://codesandbox.io/s/react-state-e1-cbfhlg)

</details>

---

### Day 6: 9th Feb 2023
<details>

**Today's Progress**: 
* Continue to finish the exercise on [React Beta Doc about the State](https://beta.reactjs.org/learn/state-a-components-memory).

**Thoughts:** 
* The last exercise is a bit interesting. In this exercise, I tried to recreate the same React again by using state (It's a TRAP!). But it's not correct. **Don’t introduce state variables when a regular variable works well!** 


**Link to work:** 
1. 2nd Exercise- [React beta- State Exercise 2](https://codesandbox.io/s/react-state-e2-rs2t7c?file=/App.js)
2. [3rd Exercise](https://codesandbox.io/s/react-state-e3-qxlv8h)
3. [4th Exercise](https://codesandbox.io/s/react-state-e4-z0vt1d)

</details>

---

### Day 7: 10th Feb 2023
<details>

**Today's Progress**: 
* Did coding challenge & wrote test to test my own solution.

**Thoughts:** 
**Coding Challenge**
1. Did a coding challenge today on Codewars. I was confident but actually my JS skill becomes rusty again. Made me feel like I should really do at least 1 coding challenge each day! (But sometime I spent a lot of time in 1 question!). 
```hasOwnProperty()``` - to check whether is object has a certain key/property.
2. I learnt some testing (Vitest) so I wrote 2 simple tests for my solution. Felt good but again rusty!
```toStrictEqual()``` and ```toEqual()``` - both only compares the values and good to use when testing object. But ```toStrictEqual()``` will also compare the datatype of the value and able to notice "undefined" and "null" value.
 


**Link to work:** 
1. [Codewars-Coding Challenge with test](https://www.codewars.com/kata/reviews/52efefcbcdf57161d4000094/groups/63e5ba57bfb4790001458a94)

</details>

---

### Day 8: 11th Feb 2023
<details>

**Today's Progress**: 
* I did not do much today as I was working the whole day. I only did a simple react exercise.

**Thoughts:** 
1. Just did a very simple exercise. Tried to read [State as Snapshot](https://beta.reactjs.org/learn/state-as-a-snapshot) but I cant really focus.


**Link to work:** 
1. [React-Simple Exercise](https://codesandbox.io/s/react-state-as-snapshot-practice1-1evqjp?file=/src/App.js) from [here](https://beta.reactjs.org/learn/state-as-a-snapshot).

</details>

---

### Day 9: 12th Feb 2023
<details>

**Today's Progress**: 
* First time trying Frontend Mentor and did my first challenge! Mostly trained on my CSS skill.

**Thoughts:** 
**Frontend Mentor**
1. ```box-shadow```: cant use %.
2. Syntax: ```box-shadow: [horizontal offset] [vertical offset] [blur radius] [optional spread radius] [color];```

**Link to work:** 
1. 

</details>

---

### Day 10: 13th Feb 2023
