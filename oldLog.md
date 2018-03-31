#This is the old log to my first attempt at #100daysofcode. Recorded here for
# posterity?

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
Totally embarrassed. Well, it's all roses from here, haha.

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
working through iterating through a list of users. More so, I want to define
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
Going forward, I'll try to avoid callback hell. It will also help me pass data
around.

**Helpful Resource of the Day**: [net ninja async-js tutorial](https://www.thenetninja.co.uk/courses/asynchronous-javascript-tutorial)

**Link to work:** [weather javascript without callback hell](http://bradleyhop.github.io/weatherApp/weather.js)

### Day 6: June 30, 2017

**Today's Progress**: Replaced large switch statement in weather app with object
literal, which is easier to read and less code.
Finally getting consistent info on channel online status in twitch app. Now to
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

**Thoughts**: Decide to use an accordion to display user and channel information.
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

**Today's Progress**: Lots. Added css, using a Material design color palette,
using my own for additional colors based on pallet design. Added Materialize
card component to display the not online accounts. Fixed preloader bar: using
indeterminate and setting height so the rest of the page doesn't pop around when
it disappears.

**Thoughts**: Dug deep into the Materialize framework today. I'm liking it
better than bootstrap. With a stronger design framework built into the css
framework, my page actually looks like it has some design!

**Link to work:**[ twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)

**Todo**: Finish composing the card components for the non-existing accounts and
the online accounts. Maybe pick some different channels.

### Day 16: July 10, 2017

**Today's Progress**: Finished the Online and Not Existing User cards.

**Link to work:**[ twitch app js](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)

### Day 17: July 11, 2017

**Today's Progress**: Tweaked the styles of the various cards so that the info
is obvious and the layout is clear. Lots of css work today.

**Thoughts**: Annoyed that the cards don't align vertically. Also, tried finding
more channels that regularly stream. The biggy is that my display functions
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

### Day 19: July 13, 2017

**Today's Progress**: Through CSS Wizardry I was able to get the cards to stack
nicely in two columns! No Masonry framework needed. However - there does seem to
be some wonkiness in alignment, and the solution (and the page overall) isn't
very responsive. Though, responsiveness is not a requirement for the project, I
would like a bit closer to it.

Also, I had my first git merge conflict. I think it was when I worked on the
master branch and went ahead and committed it. The next day, committing the
working branch gave the conflict error. I had to look up the help on github,
which lead me manually edit some files. Finally got it resolved and the repro up
to date. I did cheat tho: I copied the most recent change to a different
directory not in the local repo and then copied it back over once I resolved the
conflict. At any rate, fixed it.

**Link to work:**[ twitch app js, ](https://bradleyhop.github.io/twitchOnline/onlineTwitch.js)
[ twitch html, ](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)
[ twitch css](http://bradleyhop.github.io/twitchOnline/styleTwitch.css)
[, git hub repro](https://github.com/bradleyhop)

### Day 20: July 14, 2017

**Today's Progress**: Actually fixed the merge conflict that I started the night
before. Tried stackoverflow, but really help.github was the best resource.

Fixed bugs in twitch javascript. Played with column setting to maximize pretty
flow. I think I have it as good as its going to get. The whole page isn't very
responsive now, though. Not sure I care enough at this point to fix it. Cards
within the columns now have proper widths and borders, etc.


**Link to work:**[ twitch app ](https://bradleyhop.github.io/twitchOnline/)
[, git hub repro](https://github.com/bradleyhop)
[, weather app](https://bradleyhop.github.io/weatherApp/)

### Day 21: July 15, 2017

**Today's Progress**: Tweaked CSS further on twitch app. Adjusted colors,
margins, etc. Big lesson learned is the use of columns with just css. The app
renders just fine on mobile (chrome dev responsive tool wouldn't render
correctly - may have to do with on load vs resize).

Finished the Twitch app! (basically, haha) I still want to fix the twitch logo
image (tends to run into text on smaller sizes), and am tempted to add a search
bar. (Keep telling myself it won't take that long...). Finally, added twitch app
to project landing page.


**Link to work:**[ twitch app ](https://bradleyhop.github.io/twitchOnline/onlineTwitch.html)

### Day 22: July 16, 2017

**Today's Progress**: Going back to portfolio page and tweaking CSS. Seriously
considering switching to materialize from bootstrap. Used phantomjs to take
screenshots of apps using its server. They don't plug in well to bootstrap's
card component. Also, tried to get twitch img logo to flow around the text
next to it. I'm guessing I need to use separate columns rather than the same.
(pushed but didn't merge)

**Link to work:** [ portfolio page ](htts://bradleyhop.github.io)

### Day 23: July 17, 2017

**Today's Progress**: Fun with regular expressions. Glad to have nodeschool to
help. Most cases solved, trying to get the last few esp. unmatched parens.

**Link to work:**[ validateUSPhoneNumber.js ](https://github.io/bradleyhop/freecodecamp/advancedAlgoScript)

### Day 24: July 18, 2017

**Today's Progress**: Finished a adv algorithm challenge ala fCC. Used [regexr](regexr.com)
to write a regular expression to validate us phone numbers. Also, started the
React course on codeccademy. Wanna learn some components!

Revisited Twitch app: wrapped twitch logo link in a div so no overflow on smaller
screen sizes.

**Link to work:**[ validateUSPhoneNumber.js ](https://github.io/bradleyhop/freecodecamp/advancedAlgoScript)
[codeccademy react](codeccademy.com)

### Day 25: July 19, 2017

**Today's Progress**: Started the exact change and the symmetric difference
advanced algorithm challenges. Exact change is set for equal or insufficient
funds, but need to start stepping through the cid array and construct a given
change array. For the sym diff, can only check the first given array against the
second, not the other way around as well.

**Link to work:**[ advanced algo challenges ](github.com/bradleyhop/freeCodeCamp/advancedAlgoChallenges)

### Day 26: July 20, 2017

**Today's Progress**: Worked on the exact change fCC algorithm.
Tweaked fCC projects: Added image wrapper to twitch logo on twitch app. Improved
scoping in weather app. Update materialize cdn release for twitch app.

**Link to work:**[ landing page ](https://bradleyhop.github.io)

### Day 27: July 21, 2017

**Today's Progress**: Start to work on symmetrical difference in earnest. Can
only get the difference from one array, but not from both.


**Link to work:**[ sym diff ](https://github.com/bradleyhop/freeCodeCamp/advancedAlgoChallenges/)

### Day 28: July 22, 2017

**Today's Progress**: None.

**Thoughts**: I've decided I'm not going to stress out about it. According to
the FAQ, I'm allowed to miss one day (but not two) so long as I add another. So,
Day 28 shall be repeated. Got to keep my eye on the goal that I'm developing a
habit.

### Day 28: July 23, 2017

**Today's Progress**: Finished symmetrical difference algorithm challenge! I was
not clearly understanding the mathematical def of a sym diff. Once I understood,
was able to get the sym diff of two sets (arrays), and from that set get the sym
diff of another set (array), if given, etc. Had to trim doubles, so added helper
function.

**Link to work:**[ sym diff ](https://github.com/bradleyhop/freeCodeCamp/advancedAlgoChallenges/)

### Day 29: July 24, 2017

**Today's Progress**: Modified styling for portfolio page: Changed the colors
of the card components so it won't match the screenshot of the project (esp the
twitch app). Fixed broken links to screenshots. Using codepen's screenshot
feature to grab png for assets.

**Link to work:**[ landing page ](https://bradleyhop.github.io)

### Day 30: July 25, 2017

**Todays' Progress**: Started the 'no repeats please' fCC challenge. Added
 100 Days Of Code section to the portfolio/landing page. Styled section,
cleaned up the css file. Added Google analytics tracker, tho not sure if it's
working. (No visits yet)

**Link to work:**[ landing page, ](https://bradleyhop.github.io)[ no repeats please ](https://github.com/bradleyhop/freeCodeCampAlgorithms)

**Thoughts**: I'm scared to share my commitment and portfolio page to facebook.
I want to present a finished product, not a work in process. However, its about
the journey, right? Maybe instead of giving daily updates, I can share one
project a week? It can only help to get my name out there.


### Day 31: July 26, 2017

**Today's Progress**: Finished the 'no repeats please' fcc challenge! Looked up
the algorithm for finding permutations in pseudo-code. Wrote the javascript from
that. I had more trouble getting the regular expression to work. Just when you
think you know something...

**Link to work:**[ no repeats please ](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 32: July 27, 2017

**Today's Progress**: Finished two advanced algorithm challenges!! 'Make A
Person' and 'Map the Debris'!!! For makeAPerson.js, reading through Eloquent
Javascript was a huge help. I want to solve the problem in a different way, but
it was good to code it to fCC's specs. For mapTheDebris.js, once I figured out
which equation to use, it became much easier. First, I computed the orbital
period for one input. From there, I just looped through the rest only changing
the arr element access. Also, the delete keyword was new to me. So simple.

**Link to work:**[ map the debris ][, makeAPerson ](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 33: July 28, 2017

**Today's Progress**: Finished the Inventory Update adv algorithm challenge for
fCC. I was trying to solve the problem all in one go. What happened instead was
that I kept adding elements to an array and never stopped! Once I broke the
problem down into the right chucnks, it was much easier. Upadating the stock on
an item present in both arrays was easy. Seeing if an item in the new stock was
in the old stock was more difficult. I used a couple of intermediary arrays to
store names of items, then checked for indeces of names in the old stock.
Frustrating, but satisfying!

**Link to work:**[inventoryUpdate](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 34: July 29, 2017

**Today's Progress**: Continue to work on Exact Change fCC adv algorithm. Not
getting very far. I think that I'm trying to do everything 'in place'. Calculate,
then immediately use. That might be the hard way. At any rate, resorted to pencil
and paper method. It helped me plan things out. And replan...

**Link to work:**[inventoryUpdate](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 35: July 30, 2017

**Today's Progress**: Little. Looked at exact change algorithm, but not long
enough. Today counts as a skip day.

### Day 35: July 31, 2017

**Today's Progress**: Actually made headway on exact change. I can get an array
to return with the proper amounts based on the value of the denomination. But.
The cash in the drawer doesn't always have the full amount of that denomination
to subtract before going on to the next.

**Link to work:**[inventoryUpdate](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 36: July 31, 2017

**Today's Progress**: Hacking away at the same problem. Took a break for a while
and worked on the portfolio site. Improved readability and added a button on
contacts for twitter.

**Link to work:**[inventoryUpdate](https://github.com/bradleyhop/freeCodeCampAlgorithms)
[ portfolio ](https://bradleyhop.github.io)

### Day 37: August 1, 2017

**Today's Progress**: Portfolio Site: changed styling for readablity; added
Twitter button. Exact Change challenge: can get change based on value of
denomination, but not on what's actually available in drawer.

**Link to work:**[exact change](https://github.com/bradleyhop/freeCodeCampAlgorithms)
[ portfolio ](https://bradleyhop.github.io)

### Day 38: August 2, 2017

**Today's Progress**: Finished Exact Change challenge! Part of my problem was
in not converting the cash-in-drawer array to pennies. Added function to mapping
earlier in program.

**Link to work:**[exact change](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 38: August 3, 2017

**Today's Progress**: Acutally started a new job today. Its a better gig, and
I'll be happier here. Too excited; ended up not coding long enough to count :(

### Day 39: August 4, 2017

**Today's Progress**: Fixed broken links in card component builder function. (I
really need to learn React...). Did research in React vs Vue. I'm going to learn
React b/c I see more job opening for that than I do Vue. I found a tutorial on
youtube and I'm going to give that a go.

Also started the last algorithm challenge for fCC's front end program: Pairwise.
I see recursion as a possible tool, but I really need to sit down and plan this
bit by bit.

**Link to work:**[ portfolio ](https://bradleyhop.github.io)

### Day 40: August 5, 2017

**Today's Progress**: Switched to more reliable cors proxy on weather app. Also
refined, add template literals to code.

**Link to work:**[ portfolio ](https://bradleyhop.github.io)

### Day 41: August 6, 2017

**Today's Progress**: Worked on pairwise fCC algorithm script. About half done.
Can solve most cases except when there is more than one pair of the same number.
Pushed but didn't pull request.

**Link to work:**[exact change](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 42: August 7, 2017

**Today's Progress**: Finished Pairwise algrorithm script! Achievement unlocked:

# Finished All of freecodecamp's JavaScript Algorithm Scripting Challenges!!! #

**Link to work:**[exact change](https://github.com/bradleyhop/freeCodeCampAlgorithms)

### Day 43: August 8, 2017 ###

**Today's Progress**: Returned to Twitch app. It really bothers me that I don't
have a search field for this app. I really want to use materialize's form input,
so I've started to add a search form. Having trouble getting to style (change
colors) of the elements I want. Apparently, using the SASS code makes it easy,
but I'm using the ole CSS so I have to do a bit of digging to see what to change.

### Day 43: August 9, 2017 ###

**Thoughts**: Missed today. Job training, actual job, band gig made for a very
long day. Trying not to get down on myself.

### Day 44: August 10, 2017 ###

**Today's Progress**: Finished styling the search bar for the Twitch app. Swtiched
from string literals to template literals. Besides actually using React or similar,
template literals seem to be my best bet on keeping my html code straight when
constructing components.

**Link to work:**[ portfolio ](https://bradleyhop.github.io)

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
