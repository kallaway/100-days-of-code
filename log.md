# 100 Days Of Code - Log

### Day 1: 4th Feb 2023
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
 
---
 
 ### Day 2: 5th Feb 2023

**Today's Progress**: Continue with Conditional Rendering. Did a weather exercise and did some vanilla CSS styling to it. Read passing props to components but I'm still a bit confused. Will read more & watch some videos tomorrow.

**Thoughts:** 
1. I had some trouble to do the Weather Forecast exercise. Couldnt get the Switch stmt working but got it worked eventually. But still my skill is abit rusty.
2. Felt good to use vanilla CSS to style this. 1 thing I will take out from this is how to add background-image and how to make background-image not repeating and cover.
3. Read the docs on React Beta - Passing props to a Components and done 2 exercises. I still cant really understand and will read more tomorrow.

**Link to work:** 
1. [React-Weather Forecast](https://codesandbox.io/s/w7d2-weather-forecast-again-oeo0d8?file=/src/styles.css)
2. [React: Passing props to component exercise 1](https://codesandbox.io/s/react-passingprops-e1-pxeqk9)
3. [React Beta - Passing JSX as children](https://codesandbox.io/s/reactbeta-passingjsxchildren-bpulxm)

---

### Day 3: 6th Feb 2023

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


---

### Day 4: 7th Feb 2023


**Today's Progress**: 
* Done some coding challenges & APIs.

**Thoughts:** 
* Not much coding today. Did 1 coding challenges, learnt "flattening an array" is to reduce the dimensionality of an array. Can use .flat() or reduce method. 
* I learnt some API today as I'm always confused about API.

**Link to work:** 
1. [Codewars-Flattening the array](https://www.codewars.com/kata/reviews/5251f603dc71afdb4f0002d5/groups/63e18ebb17b96d000140ee47)
2. [APIs for Beginner](https://www.youtube.com/watch?v=WXsD0ZgxjRw)


---

### Day 5: 8th Feb 2023


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



---

### Day 6: 9th Feb 2023


**Today's Progress**: 
* Continue to finish the exercise on [React Beta Doc about the State](https://beta.reactjs.org/learn/state-a-components-memory).

**Thoughts:** 
* The last exercise is a bit interesting. In this exercise, I tried to recreate the same React again by using state (It's a TRAP!). But it's not correct. **Don’t introduce state variables when a regular variable works well!** 


**Link to work:** 
1. 2nd Exercise- [React beta- State Exercise 2](https://codesandbox.io/s/react-state-e2-rs2t7c?file=/App.js)
2. [3rd Exercise](https://codesandbox.io/s/react-state-e3-qxlv8h)
3. [4th Exercise](https://codesandbox.io/s/react-state-e4-z0vt1d)



---

### Day 7: 10th Feb 2023


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



---

### Day 8: 11th Feb 2023


**Today's Progress**: 
* I did not do much today as I was working the whole day. I only did a simple react exercise.

**Thoughts:** 
1. Just did a very simple exercise. Tried to read [State as Snapshot](https://beta.reactjs.org/learn/state-as-a-snapshot) but I cant really focus.


**Link to work:** 
1. [React-Simple Exercise](https://codesandbox.io/s/react-state-as-snapshot-practice1-1evqjp?file=/src/App.js) from [here](https://beta.reactjs.org/learn/state-as-a-snapshot).



---

### Day 9: 12th Feb 2023


**Today's Progress**: First time trying Frontend Mentor and did my first challenge! Mostly trained on my CSS skill. Felt good about it!

**Thoughts:** 
**Frontend Mentor**
1. ```box-shadow```: cant use %.
2. Syntax: ```box-shadow: [horizontal offset] [vertical offset] [blur radius] [optional spread radius] [color];```
3. Learnt something about I could not overcome today by doing this exercise. [To center my card](https://stackoverflow.com/questions/75425590/css-height-calc100vh-1px-will-make-element-to-be-center-but-why)

**Link to work:** 
1. [My challenge link on Frontend Mentor](https://www.frontendmentor.io/solutions/responsive-qr-code-component-pdQfMj5vYE)
2. [My Github link](https://github.com/AdoraWyne/frontendMentor-QR-code-component)
3. [The Live URL](https://adorawyne.github.io/frontendMentor-QR-code-component/)



---

### Day 10: 13th Feb 2023


**Today's Progress**: Tried to do Accordion on React to play with the states, which was quite hard to understand in my opinion. I should give it a go later to see if I still understand it.

**Thoughts:** 
**Sharing state between components**
1. Lift the state to the closest common parents & pass the state down to child component as props.
2. To change the shared state in each child component, need to pass down an event handler as props too to the child component, so the shared state can be updated in each child component.
[React Beta Doc](https://beta.reactjs.org/learn/sharing-state-between-components) has some explanation but I think [Mickey](https://codesandbox.io/s/accordion-forked-j7emxo) or my example bellow is clearer. 

**Link to work:** 
1. Recreated the [example](https://codesandbox.io/s/react-beta-accordion-example-1qx2r3?file=/src/App.js)
2. My own [Accordion example](https://codesandbox.io/s/w7d3-lab-accordion-again-2hqsdx?file=/src/components/ContentPanel.js)



---

### Day 11: 14th Feb 2023


**Today's Progress**: 
1. Tried another Frontend Mentor challenge. I was 95% done. Mostly practice on my vanilla CSS skill. 
2. Need to watch Kevin Powell's video how to solve the remaining 5% and how his thought process and the way he approached.
  
**Thoughts:** 
1. This challenge is very similar to the first challenge I did. But I'm still not really good at planning or organising the HTML element or classes for styling. 
2. I was kind of code as I go - i.e. I styled from the top to bottom based on the mobile version picture. So if I realised there is a problem, I will fix it, but it might potentially cause another problem, then I will need to fix it again. 
3. I would say this is probably not a good coding habit or practice. 
4. Thankfully, I found that Kevin Powell has done the same challenge. As I watched through the first 30mins, I have already learned so much. Structured your HTML first, how to need the class name, [reset your CSS](https://www.joshwcomeau.com/css/custom-css-reset/), etc.


**Link to work:** 
1. [My Frontend Mentor Product Card Component](https://github.com/AdoraWyne/fM-product-card-component)



---

### Day 12: 15th Feb 2023


**Today's Progress**: 
1. Done watching Kevin Powell's video how to approach the challenge and I learnt a lot. I was thinking to redo the challenge with all the these things I just learned but I decided not to but will use the new knowledge I learnt on the next challenge!
2. Also, I received my very first interview today and spent 30-mins being so excited & happy, jumped around the house, and spent another few hours doing research on the company. HAPPIEEE!
3. Therefore, I took an easy way today by just completing the Frontend Mentor coding challenge and another Leetcode coding challenge.

**Thoughts:** 
**Leetcode challenge** 
1. Did not know we cannot call ```.length``` on numbers! Have to convert it to string and run string.length.
2. This is such a simple question but I took a while! Need to do more coding challenge again!


**Link to work:** 
1. [My Frontend Mentor Product Card Component](https://github.com/AdoraWyne/fM-product-card-component)
2. [Frontend Mentor site](https://www.frontendmentor.io/solutions/product-card-component-jmuvctP8RB)
3. [Leetcode: Palindrome Number](https://leetcode.com/problems/palindrome-number/solutions/)



---

### Day 13: 16th Feb 2023


**Today's Progress**: 
1. Did coding challenge on Codewars.

**Thoughts:** 
**Codewars - Square(n)Sum**
1. It's been a while since I did coding challenge, so I started with something easy. Thankfully, my skill is still there (but not quite)! 
2. Used reduce method to solve this problem easily, BUT! I made a small mistake here but neglecting the initial value:

- This is my initial approach. 
- I passed the test but I did not passed all the random tests after I clicked "Attempt".
- I was wondering why. Why after I added initial value as 0, then only I will pass the test?
```js
function squareSum(numbers){
  
  if (numbers.length === 0) return 0;
  
  return numbers.reduce((accumulator, currentValue) => {
    return accumulator + currentValue**2
  })
}
```
- Then I figured it out! Because if I did not put the initial value, it will take the Array[0] first element as the initial value. And it will not square the first element or number! That's why I kept failing the test!
- Here is my final solution, nice and clean!
```js
function squareSum(numbers){
  return numbers.reduce((accumulator, currentValue) => {
    return accumulator + currentValue**2
  },0)
}
```
- I wrote test for it too but they are very simple:
```js
import {it, expect} from 'vitest';
import {squareSum} from './testing'

it('should return the total sum of squared number in the array', () => {
    const input = [2,3]

    const result = squareSum(input)

    expect(result).toBe(13)
})

it('should return 0 when the array is empty', () => {
    const input = []

    const result = squareSum(input)

    expect(result).toBe(0)
})

it('should return the correct sum when one of the elements is negative number', () => {
    const input = [-1, -2]
    
    const result = squareSum(input)

    expect(result).toBe(5)
})
```
- Also rewrite in TS because it is fairly easy
```ts
function squareSum(numbers: number[]): number{
    return numbers.reduce((accumulator, currentValue) => {
        return accumulator + currentValue**2
    },0)
}
```

**Link to work:** 
1. [Codewars - Square(n)Sum](https://www.codewars.com/kata/515e271a311df0350d00000f/javascript)



---

### Day 14: 17th Feb 2023


#### Today's Progress:
1. Did 2 coding challenge on Codewars.
2. TBH, started yesterday, I start to feel like it's hard to commit code 1 hour & feel like I want to skip. 😬
3. Despite of that, I coded almost 3 hours today. Felt good~ 🤩


#### Thoughts:
**Codewars - Numbers to Letters**
1. The hardest part of this kata is find a way to arrange the alphabets with its numbers but not try to hard code it. 
2. I did hard code it at first. But when I looked at the solution, it's just so easy! I never thought of that. 
3. Here is my initial approach: Basically hard coded my alphebets part.
```js
const word = {
  "29":" ",
  "28":"?",
  "27": "!",
  "26": "a",
...
}

function switcher(x){
  let words = ""
  for (let item of x) {
    words += word[item]
  }
  return words
}
```

4. Then I changed to this: Nice and clean!
```js
function switcher(x){
  const alphabets = ' zyxwvutsrqponmlkjihgfedcba!? '
  return x.map(item => alphabets[item]).join("")
}
```


**Codewars - Numbers of Letters of Numbers**
1. The hardest part of this kata is the last step where you need to we have reached a stable equilibrium. (where a state in which a program or system remains balanced or unchanged despite perturbations or disturbances.)
2. From the kata, I thought just compare the length of the last 2 elements in the array would be fine. 
3. It was fine, but not for 1 test case where the input is 4.
4. My initial approach:
```js
function numbersOfLetters(integer) {
  let wordsInArray = []
  // Just to convert number to word -> 1 to "one"
  function convertToString(number) {
    switch(number){
      case "0":
        number ="zero";
        break;
        case "1":
        number ="one";
        break;
        case "2":
        number ="two";
        break;
        case "3":
        number ="three";
        break;
        case "4":
        number ="four";
        break;
        case "5":
        number ="five";
        break;
        case "6":
        number ="six";
        break;
        case "7":
        number ="seven";
        break;
        case "8":
        number ="eight";
        break;
        case "9":
        number ="nine";
        break;
        default:
        alert("please enter a valid number")
    }
    return number;
  }
  // Combine words together -> 11 to "oneone"
  function combineNumberWords(integer){
	  let numbersInArray = String(integer).split("")
	  let numbersInWords = ""
	  for (let item of numbersInArray) {
		  numbersInWords += convertToString(item)
	  }
  	return numbersInWords
  }
  wordsInArray[0] = combineNumberWords(integer)
  wordsInArray[1] = combineNumberWords(wordsInArray[0].length)
  let i = 1;
  while(wordsInArray.slice(-1)[0].length !== wordsInArray.slice(-2,-1)[0].length) {
    wordsInArray.push(combineNumberWords(wordsInArray[i].length));
    i++
  }
    return wordsInArray
}
```

5. But this will fail the test case where input is 4. The result I get is ```["four", "four"]``` but the correct answer is ```["four"]```.
6. So I modified by adding a IF ELSE statement. But I still don't know understand why ```["four", "four"]``` is not correct.
7. Is it something to deal with the stable equilibrium?


#### Link to work:
1. [Codewars - Numbers to Letters](https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/solutions/javascript?filter=me&sort=best_practice&invalids=false)
2. [Codewars - Numbers of Letters of Numbers](https://www.codewars.com/kata/599febdc3f64cd21d8000117/solutions/javascript?filter=me&sort=best_practice&invalids=false)


---

### Day 15: 18th Feb 2023

