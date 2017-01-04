# 100 Days Of Code - Log

<!-- TOC -->

- [100 Days Of Code - Log](#100-days-of-code---log)
        - [Day 0: 2016-12-30](#day-0-2016-12-30)
        - [Day 1: 2016-12-31](#day-1-2016-12-31)
        - [Day 2: 2017-01-01](#day-2-2017-01-01)
        - [Day 3: 2017-01-02](#day-3-2017-01-02)
        - [Day 4: 2017-01-03](#day-4-2017-01-03)
        - [Day 5: 2017-01-04](#day-5-2017-01-04)
        - [Day 6: 2017-01-05](#day-6-2017-01-05)

<!-- /TOC -->

### Day 0: 2016-12-30

**Today's Progress**: I went through the FreeCodeCamp jQuery exercises again then started the 'Show the Local Weather' FreeCodeCamp challenge.

So far I have HTML file with a couple of div's and JavaScript file that fetches the [openweathermap](https://openweathermap.org/current#geo) data with ~~hard coded lat and long values~~

I used [ip-api.com](http://ip-api.com/json) to get my geo data which I have struggled to have a separate functions so now its functions in functions.

**Thoughts**: Not a fan of jQuery, oh wait it's not that bad when it works, but $ this and $ that everywhere and functionception everywhere!

**Up Next**: Work with the JSON data and do some nice stuff with that!

**Link(s) to work**: 

[My FreeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/FreeCodeCamp/tree/master/Show%20the%20Local%20Weather)

[The CodePen pen](http://codepen.io/spences10/pen/WoVRNq)

---

### Day 1: 2016-12-31

**Today's Progress**: Looking at weather icons, still not sure on how to do this, I also had to change from using [ip-api.com](ip-api.com) to [freegeoip.net](freegeoip.net/) as [ip-api.com](ip-api.com) was showing me as ~100 miles away from my current location.

Completed Location, Weather type, and temp, ~~just looks like crap still!~~ 

Added a [random image function](https://gist.github.com/spences10/d48af132d0fc3f227e1c72733a356802) from flickr, added styling into the JavaScript looks ok on both my machine and CodePen :sparkles: :astonished: :sparkles:

**Thoughts**: Working with APIs is becoming a bit more straightforward with jQuery as long as there is a JSON object to work with. I :heart: the Chrome dev console! Has really helped me with debugging.

**Up Next**: ~~Style it yo!~~ Onto the next FCC challenge by the looks of it now!

**Link(s) to work**: 

[My FreeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/FreeCodeCamp/tree/master/Show%20the%20Local%20Weather)

[The CodePen pen](http://codepen.io/spences10/full/WoVRNq/)

---

### Day 2: 2017-01-01

**Today's Progress**: Set up repo for the FreeCodeCamp(:fire:) Zipline 'Build a Wikipedia Viewer', added HTML, CSS and JS files to the repo, added a search box and a random article button. 

**Thoughts**: @wesbos has a type ahead example I went through with the #JavaScript30 tutorials which may come in handy, or just use a jQuery/Ajax example

**Up Next**: Get the data working! Ajax ftw?

**Link(s) to work**: 

[My FreeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/FreeCodeCamp/tree/master/Wikipedia%20Viewer)

---

### Day 3: 2017-01-02

**Today's Progress**: FreeCodeCamp(:fire:) Wikipedia Viewer: Added a getJSON function to the js file, can console log the data but it's only one result at a time

Twitter bot: Had a look at making a twitter bot with [twitter-bot-bootstrap](https://github.com/mobeets/twitter-bot-bootstrap) was quite interesting playing with Heroku and deploying my app, a broken app! 

Git-it: I still use Git as ```git commit``` and ```git push origin master``` and struggle with branching and pull requests [Git-it](http://jlord.us/git-it/index.html) is really helpful in getting you comfortable with forking and PRs, I still need to play with it a lot more.

**Thoughts**: Shit progress is shit! I spent all that time yesterday making the page look pretty but didn't actually think about what else to do hoping that it would magically come to me today.

**Up Next**: Same as today

**Link(s) to work**: 

[My FreeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/FreeCodeCamp/tree/master/Wikipedia%20Viewer)

---

### Day 4: 2017-01-03

**Today's Progress**: 

AM: Completed the follow through of @amandeepmittal's [Twitter bot pt 1](https://hackernoon.com/create-a-simple-twitter-bot-with-node-js-5b14eb006c08#.k7ge75k9d) in my c9 Node.js set up. Created GitHub repo for the project then deployed to Heroku

PM: Followed the second part of @amandeepmittal's [Twitter bot pt 2](https://community.risingstack.com/how-to-make-a-twitter-bot-with-node-js/) created and deployed app to Heroku, attempted to make the query string for the tweets and failed miserably, tweaked the timings on retweets and favorites and now I'm not sure if ```setTimeout``` function is hitting the API too often, I have dialed back the frequency now.

Some gotcha's with this: if deploying to Heroku use a ```Procfile``` set the process as a ```worker``` as the default is ```web``` and you will get crashes.

My ```Procfile```:

```
worker: node bot.js
heroku ps:scale worker=1
```

**Thoughts**: GIT Gah!! I made a mess on my tweetbot repo by adding a url with security token to my blog repo then was confused as to why the origin wasn't up to date with the master when I thought the master was empty, so I used ```git push --force``` and overwrote the repo :scream: luckily I had a clone on my phone of the blog repo so I was able to push it back :relieved:

**Up Next**: See how the bot does overnight then decide weather ot not to tweak it some more.

**Link(s) to work**: 

[My GitHub repo](https://github.com/spences10/spences10-twitter-bot)

---

### Day 5: 2017-01-04

**Today's Progress**: 

**Thoughts**: 

**Up Next**: 

**Link(s) to work**: 

---

### Day 6: 2017-01-05

**Today's Progress**: 

**Thoughts**: 

**Up Next**: 

**Link(s) to work**: 

