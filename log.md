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
* Done some coding challenges

**Thoughts:** 
* 

**Link to work:** 
1. [Codewars-Flattening the array](https://www.codewars.com/kata/reviews/5251f603dc71afdb4f0002d5/groups/63e18ebb17b96d000140ee47)
2. 
</details>

---

### Day 5: 8th Feb 2023

