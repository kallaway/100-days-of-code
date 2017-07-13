#100 Days Of Code - Log

### Day 0: June 24, 2017

**Today's Progress**: Uploaded landing page/ portfolio to github. Made edits to
project cards, fixed typos, etc.

**Thoughts**: I feel very insecure about putting myself out here, but I also
feel that I'm coding in a vacuum. I also feel that I'm not ready, since I don't
list every project I've completed for freecodecamp (fCC) on my landing page.
But-- better to publish and add features as I go rather than to never publish at
all.

**Link to work:** [portfolio page](http://bradleyhop.github.io)

**Update**: Tried to push my own master branch to the actual master branch.
Totally embaressed. Well, it's all roses from here, haha.

### Day 1: June 25, 2017

**Today's Progress**: Downloaded code for my weather app from codepen.io. Added
code so that it functions as a stand-alone webpage. Also, fixed the colors on
my wiki search app.

**Thoughts**: Looks like github doesn't count contributions you make when you
check in code from your master branch. I uploaded the new weather app, but it
didn't show progress. So I made some color changes on the wiki app, and pushed
that. Slowly learning git and making it secondhand knowledge.

Already, I'm doubting myself. I came home, fed the cat, sat down, and started
the pomodoro timer. That timer is what keeps me going, as long as I can start.

**Link to work:** [weather app](http://bradleyhop.github.io/weatherApp/weather.html)

### Day 2: June 26, 2017

**Today's Progress**: Worked on twitch app for freecodcamp front end project.

**Thoughts** : I've been able to get data from the twitch api, but now I'm
working through iterating through a list of users. Moreso, I want to define
actions, namely building a html status box, based on a user's online status. So
 far, not successful.

Did learn about ajax deferred callbacks, .done .error, and .then (which seems to
be a catchall). All learned that api's can block you for too many calls. Need to
figure out how to pause codepen.io's autorefresh. Codepen is useful for getting
these object calls and seeing how they return.

Was also very tired tonight. Full day of work, and then teaching, and then
coding. Almost feel asleep.

**Link to work:** [twitch app js only](http://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 3: June 27, 2017

**Today's Progress**: Continue work on twitch app for fCC

**Thoughts** : Still having trouble getting online status for each channel. I
can get the json's from the api one at a time, but when I check to see if status
returns an object with stream:null... blarg. I'm testing with a function call
using ajax, but the test completes before the function call does. Async. Blarg.

**Link to work:** [twitch app js only](http://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 4: June 28, 2017

**Today's Progress**: Continue work on twitch app for fCC. Start to add json for
projects for portfolio page.

**Thoughts** : Having troubles with javascript's async behavior. Going to ask
the fCC forum.

**Link to work:** [twitch app js only](http://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 5: June 29, 2017

**Today's Progress**: Learning much about javascripts asynchronus behavior.
Finally found a resource to help me understand. Refactored weather app's js to
try out new skills. No more nested ajax calls! But still, not perfect. Onto
learning about promises!

**Thoughts** : fCC forum is great. Its the stackoverflow for code noobs like me.
Going foward, I'll try to avoid callback hell. It will also help me pass data
around.

**Helpful Resource of the Day**: [net ninja async-js tutorial](https://www.thenetninja.co.uk/courses/asynchronous-javascript-tutorial)

**Link to work:** [weather javascript without callback hell](http://bradleyhop.github.io/weatherApp/weather.js)

### Day 6: June 30, 2017

**Today's Progress**: Replaced large switch statement in weather app with object
literal, which is easier to read and less code.
Finally getting consistant info on channel online status in twitch app. Now to
design and code based on this info. Also, need to check if valid channel!

**Thoughts** : I think I return to old projects and refine the old code when I'm
trying to avoid the current project I'm supposed to be focusing on. I feel kinda
guilty, but also I'm still learning and applying -- using what I learn now to
fix old messes.

**Link to work:** [weather app with object literal](http://bradleyhop.github.io/weatherApp/weather.js) [  twitch app js getting online status](http://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 7: July 1, 2017

**Today's Progress**: Dug into twitch's api to find the info that I need.

**Thoughts** : I'm really not digging twitch. There's a lot of info to dig
through, even though I don't need it all. Taking time to design how I want to
display the results and structure the code is helping me not feel overwhelmed.

**Link to work:** [twitch app](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 8: July 2, 2017

**Today's Progress**: Learned more about promises, and how to use them via
jquery. Building my own object based on user with the info I want from two
different getJSON requests. Mostly working, except no currently streaming
results, yet.

**Thoughts**: If you can't request the object you need, build one from the
objects you can get. With an array of these object, it should be straightforward
to build the html to display the info required for this project.

**Link to work:** [twitch app](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 9: July 3, 2017

**Today's Progress**: Learned about the materialize css framework. Works very
much like bootstrap -- just with more design theory overhead. Also, continue to
refine my understanding of making objects.

**Link to work:** [twitch app](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 10: July 4, 2017

**Today's Progress**: Finished local object. I now have a local object with all
the info I need to display the result the project calls for. Local object is
built with the objects called via twitch.tv api.
Also started html, setup for materialize framework.

**Thoughts**: Hard to code on a holiday, but I had to work today anyway. I'm
excited for the materialize framework, but I wonder if its going to be too much
of a distraction.

**Link to work:**[twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html setup](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)

### Day 11: July 5, 2017

**Today's Progress**: Totally finished local global object. Decided I didn't
need a key with a object value to id what user the object's info belongs to.
Just set another key for username and used the passed array element to set value.
Having trouble actually getting to those values, tho...

**Thoughts**: Decide to use an accordian to display user and channel information.
That way, I can use a slide to show certain users.
I fell asleep before pushing to git last night, so I'm updating what I did then
now. Still falls w/in the rules, right?
This twitch app is taking me so long...

**Link to work:**[twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 12: July 6, 2017

**Today's Progress**: More lessons in javascripts async behavior. Finally can
call display functions after assembling a temp object. Pass the the temp object
to the display function based on valid, offline, or online. Had to do the
conditional statements *within* the last .then promise. Anything outside that
scope *may* or *may not* execute before the getJSON's finish.

**Thoughts**: My procrastination now consists of finding new vim plugins to be
more productive with...

**Link to work:**[twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)

### Day 13: July 7, 2017

**Today's Progress**: Starting building the html for twitch app. Using tabs for
the first time. Having trouble sorting into tabs...

**Link to work:**[twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)


### Day 14: July 8, 2017

**Today's Progress**: Finished the tab html and javascript. Using Materialize
template. Gave results the correct class and appended them to the correct html
id for sorting. Essentially, done with the challenge.
Started working on a preloader progress bar via Materialize. Have to figure out
how to update, or to eliminate an indeterminate bar.

**Thoughts**: Sometimes sleeping on a problem helps. I've coded until I've
fallen asleep, laptop still in lap. There's a point where my brain shuts down,
and I can't make sense of code anymore. I shouldn't keep pressing myself to
that point. There's a long road ahead...

**Link to work:**[twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html setup](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)

### Day 15: July 9, 2017

**Today's Progress**: Lots. Added css, using a Material design color pallette,
using my own for additional colors based on pallete design. Added Materialize
card component to display the not online accoutns. Fixed preloader bar: using
indeterminate and setting height so the rest of the page doesn't pop around when
it disappears.

**Thoughts**: Dug deep into the Materialize framework today. I'm liking it
better than bootstrap. With a stronger design framework built into the css
framework, my page actually looks like it has some design!

**Link to work:**[ twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)

**Todo**: Finish composing the card compoents for the non-existing accounts and
the online accounts. Maybe pick some different channels.

### Day 16: July 10, 2017

**Today's Progress**: Finished the Online and Not Existing User cards.

**Link to work:**[ twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)

### Day 17: July 11, 2017

**Today's Progress**: Tweaked the styles of the various cards so that the info
is obvious and the layout is clear. Lots of css work today.

**Thoughts**: Annoyed that the cards don't align veritcally. Also, tried finding
more channels that regualaryly stream. The biggy is that my display functions
are really hard to maintain. I think I'm writing components, but I don't know
react or angular or vue or whatever yet, so I feel that I'm doing writing the
html to insert into the DOM the hard way. I'll make that my next step before I
start another web project.

**Link to work:**[ twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)

### Day 18: July 12, 2017
**Today's Progress**: Still annoyed that the card don't align vertically. Researched
and found that the Materialize CSS framework won't do that for me. That is, the
card will not stack so that large vertical gaps appear randomly between the
cards. So - I tweeted my delima. The Materialize Twitter account got back to me
in less than 15 minutes! Told me to look at the Masonry framework.

**Thoughts**: I feel that I'm really starting to find a community in Twitter.
I feel so inspired and encouraged, if if the likes are just people trying to push
their account or their website. I'm still getting access to the pulse of web
development! I need to hit the fCC forums more, tho.


**Link to work:**[ twitch app js, ](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html, ](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)

<!--
   -# 100 Days Of Code - Log
   -
   -### Day 0: February 30, 2016 (Example 1)
   -##### (delete me or comment me out)
   -
   -**Today's Progress**: Fixed CSS, worked on canvas functionality for the app.
   -
   -**Thoughts:** I really struggled with CSS, but, overall, I feel like I am slowly getting better at it. Canvas is still new for me, but I managed to figure out some basic functionality.
   -
   -**Link to work:** [Calculator App](http://www.example.com)
-->
