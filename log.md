# 100 Days Of Code - Log

<!-- TOC -->

- [100 Days Of Code - Log](#100-days-of-code---log)
        - [Day 000: 2016-12-30](#day-000-2016-12-30)
        - [Day 001: 2016-12-31](#day-001-2016-12-31)
        - [Day 002: 2017-01-01](#day-002-2017-01-01)
        - [Day 003: 2017-01-02](#day-003-2017-01-02)
        - [Day 004: 2017-01-03](#day-004-2017-01-03)
        - [Day 005: 2017-01-04](#day-005-2017-01-04)
        - [Day 006: 2017-01-05](#day-006-2017-01-05)
        - [Day 007: 2017-01-06](#day-007-2017-01-06)
        - [Day 008: 2017-01-07](#day-008-2017-01-07)
        - [Day 009: 2017-01-08](#day-009-2017-01-08)
        - [Day 010: 2017-01-09](#day-010-2017-01-09)
        - [Day 011: 2017-01-10](#day-011-2017-01-10)
        - [Day 012: 2017-01-11](#day-012-2017-01-11)
        - [Day 013: 2017-01-12](#day-013-2017-01-12)
        - [Day 014: 2017-01-13](#day-014-2017-01-13)
        - [Day 015: 2017-01-14](#day-015-2017-01-14)
        - [Day 016: 2017-01-15](#day-016-2017-01-15)
        - [Day 017: 2017-01-16](#day-017-2017-01-16)
        - [Day 018: 2017-01-17](#day-018-2017-01-17)
        - [Day 019: 2017-01-18](#day-019-2017-01-18)
        - [Day 020: 2017-01-19](#day-020-2017-01-19)
        - [Day 021: 2017-01-20](#day-021-2017-01-20)
        - [Day 022: 2017-01-21](#day-022-2017-01-21)
        - [Day 023: 2017-01-22](#day-023-2017-01-22)
        - [Day 024: 2017-01-23](#day-024-2017-01-23)
        - [Day 025: 2017-01-24](#day-025-2017-01-24)
        - [Day 026: 2017-01-25](#day-026-2017-01-25)

<!-- /TOC -->

### Day 000: 2016-12-30

**Today's Progress**: I went through the freeCodeCamp(:fire:) jQuery exercises again then started the 'Show the Local Weather' freeCodeCamp(:fire:)  challenge.

So far I have HTML file with a couple of div's and JavaScript file that fetches the [openweathermap](https://openweathermap.org/current#geo) data with ~~hard coded lat and long values~~

I used [ip-api.com](http://ip-api.com/json) to get my geo data which I have struggled to have a separate functions so now its functions in functions.

**Thoughts**: Not a fan of jQuery, oh wait it's not that bad when it works, but $ this and $ that everywhere and functionception everywhere!

**Up Next**: Work with the JSON data and do some nice stuff with that!

**Link(s) to work**:

[My freeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/freeCodeCamp/tree/master/Show%20the%20Local%20Weather)

[The CodePen pen](http://codepen.io/spences10/pen/WoVRNq)

---

### Day 001: 2016-12-31

**Today's Progress**: Looking at weather icons, still not sure on how to do this, I also had to change from using [ip-api.com](ip-api.com) to [freegeoip.net](freegeoip.net/) as [ip-api.com](ip-api.com) was showing me as ~100 miles away from my current location.

Completed Location, Weather type, and temp, ~~just looks like crap still!~~

Added a [random image function](https://gist.github.com/spences10/d48af132d0fc3f227e1c72733a356802) from Flickr, added styling into the JavaScript looks ok on both my machine and CodePen :sparkles: :astonished: :sparkles:

**Thoughts**: Working with APIs is becoming a bit more straightforward with jQuery as long as there is a JSON object to work with. I :heart: the Chrome dev console! Has really helped me with debugging.

**Up Next**: ~~Style it yo!~~ Onto the next FCC challenge by the looks of it now!

**Link(s) to work**:

[My freeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/freeCodeCamp/tree/master/Show%20the%20Local%20Weather)

[The CodePen pen](http://codepen.io/spences10/full/WoVRNq/)

---

### Day 002: 2017-01-01

**Today's Progress**: Set up repo for the freeCodeCamp(:fire:) Zipline 'Build a Wikipedia Viewer', added HTML, CSS and JS files to the repo, added a search box and a random article button.

**Thoughts**: @wesbos has a type ahead example I went through with the #JavaScript30 tutorials which may come in handy, or just use a jQuery/Ajax example

**Up Next**: Get the data working! Ajax ftw?

**Link(s) to work**:

[My freeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/freeCodeCamp/tree/master/Wikipedia%20Viewer)

---

### Day 003: 2017-01-02

**Today's Progress**: freeCodeCamp(:fire:) Wikipedia Viewer: Added a getJSON function to the js file, can console log the data but it's only one result at a time

Twitter bot: Had a look at making a twitter bot with [twitter-bot-bootstrap](https://github.com/mobeets/twitter-bot-bootstrap) was some what interesting playing with Heroku and deploying my app, a broken app!

Git-it: I still use Git as ```git commit``` and ```git push origin master``` and struggle with branching and pull requests [Git-it](http://jlord.us/git-it/index.html) is really helpful in getting you comfortable with forking and PRs, I still need to play with it a lot more.

**Thoughts**: Shit progress is shit! I spent all that time yesterday making the page look pretty but didn't actually think about what else to do hoping that it would magically come to me today.

**Up Next**: Same as today

**Link(s) to work**:

[My freeCodeCamp(:fire:) repo on GitHub](https://github.com/spences10/freeCodeCamp/tree/master/Wikipedia%20Viewer)

---

### Day 004: 2017-01-03

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

### Day 005: 2017-01-04

**Today's Progress**:

AM: Still gawking at my twitter feed after getting the twitter bot working, decided to do a README for the twitter bot.

PM: Gawd! I spent some time on the twitter bot today, I have documented it all [here](https://spences10.github.io/2017/01/04/twitter-mctwitbot.html) there was quite a lot that I changed from yesterday and I learned quite a lot too. Oh ana added a README for the Twitter bot!

**Thoughts**: Node.js is pretty neat, I'm very close to buying a premium c9 account.

**Up Next**: freeCodeCamp(;fire:) Wikipedia viewer zipline!! Maybe I'll add my Twitter bot to @amandeepmittal's [awesome-twitter-bots](https://github.com/amandeepmittal/awesome-twitter-bots) repo first though! :smile:

**Link(s) to work**:

[twitter-mctwitbot](https://spences10.github.io/2017/01/04/twitter-mctwitbot.html)

[My GitHub repo](https://github.com/spences10/spences10-twitter-bot)

---

### Day 006: 2017-01-05

**Today's Progress**:

AM: Forked and pulled [awesome-twitter-bots](https://github.com/amandeepmittal/awesome-twitter-bots) added my bot folder to the repo, added with `git add . ` instead of `git add myfoldername/\\*` so the folder was added as a file, I spent the next hour or so trying to work out what I did :confused:

After creating the pull request and documenting it all @amandeepmittal mentions that all I needed to do was add my repo link and Twitter link to the repo README.md :scream: then closes the pull request.

I was successfully merged this afternoon as pull [#2](https://github.com/amandeepmittal/awesome-twitter-bots/pull/2)

PM: I documented (for my own understanding really) the process of setting up a pull request on GitHub, then broke my Jekyll site messing around with the GitHub settings.

I made a post on the process here: [Git and GitHub](https://spences10.github.io/2017/01/05/git-and-github.html)

**Thoughts**: I need to branch all the things!!!

**Up Next**: Random @replies for my Twitter bot

**Link(s) to work**:

[awesome-twitter-bots](https://github.com/amandeepmittal/awesome-twitter-bots)

[Git and GitHub](https://spences10.github.io/2017/01/05/git-and-github.html)

---

### Day 007: 2017-01-06

**Today's Progress**:

AM: Used my new Git skills to branch my Twitter bot so I could add to the canned response on a follow. Added random responses to twitter-bot

I also had a look at starting again from scratch with Jekyll as I want some nice GitHub markdown and emoji's but I've somehow managed to override that theme and can't seem to get back to default

PM: Branched my changes for my #100DaysOfCode repo along with my [spences10-twitter-bot](https://github.com/spences10/spences10-twitter-bot/tree/master), set up another c9 workspace for twitter-bot-playground where I'm going to explore all the features available via [twit](https://www.npmjs.com/package/twit)

**Thoughts**: Putting off that @freeCodeCamp(:fire:) Wikipedia viewer Zipline, I don't know why :cold_sweat:

**Up Next**: Got a Cloud 9 pro licence, :smile: will have a play with that and experimenting with Node.js and probably automating my twitter bot more

**Link(s) to work**:

[Twitter-McTwitbot](https://github.com/spences10/spences10-twitter-bot)

---

### Day 008: 2017-01-07

**Today's Progress**:

AM: Created twitter-bot-playground repo, found out how to identify my own Twitter user ID from the awesome :sparkles: [twit](https://www.npmjs.com/package/twit) :sparkles: documentation.

Added some logic to [Twitter-McTwitbot](https://github.com/spences10/spences10-twitter-bot) so that it stops tweeting itself! Didn't work as I have no clue how to do callbacks :scream:

PM: Forked the [freeCodeCamp/100DaysOfCode-twitter-bot](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/) to look at some of the issues logged. Attempted to tackle issues [#3](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/3) and [#4](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/4)

**Thoughts**: Blearugh!

**Up Next**: More Twitter bot stuff

**Link(s) to work**:

[Twitter-McTwitbot](https://github.com/spences10/spences10-twitter-bot)

[twitter-bot-playground](https://github.com/spences10/twitter-bot-playground)

---

### Day 009: 2017-01-08

**Today's Progress**:

AM: Looked at the [100DaysOfCode-twitter-bot issues/](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/) and decided to take a look at [#7](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/issues/7) as bot the issues I was looking at yesterday were merged.

I created a [GitHub cheat sheet](https://gist.github.com/spences10/5c492e197e95158809a83650ff97fc3a) Gist for my most commonly used git commands.

Created a PR :octocat: for the [freeCodeCamp(:fire:) 100DaysOfCode-twitter-bot](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/pull/16)

PM: Attempted fix on [Twitter-McTwitbot](https://github.com/spences10/spences10-twitter-bot) self tweeting which I resolved by hard coding my user name into the tweet function :worried: [PR here](https://github.com/spences10/spences10-twitter-bot/pull/1)

![](https://cloud.githubusercontent.com/assets/234708/21750402/2a686626-d5aa-11e6-9758-4d7494e63c89.png)

**Thoughts**:

~~I'm knackered, this challenge is taking up all my spare time and I don't think I have made any progress over the last few days :worried:~~ Jubilant now I have resolved twitter bot issues, hopeful that my PR for [freeCodeCamp(:fire:) 100DaysOfCode-twitter-bot](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/pull/16) will be merged.

**Up Next**:

There is the [twitter-bot-playground](https://github.com/spences10/twitter-bot-playground) I was thinking about playing with more and incorporating some of the great work I have seen going into the 100DoC tweet bot that I'd like to play around with.

Then, I guess I should get back to my freeCodeCamp(:fire:) work of Wikipedia viewer zipline.

**Link(s) to work**:

[GitHub cheat sheet](https://gist.github.com/spences10/5c492e197e95158809a83650ff97fc3a)

[Twitter-McTwitbot](https://github.com/spences10/spences10-twitter-bot)

[Tweety McSelfTweet fix](https://github.com/spences10/spences10-twitter-bot/pull/1)

---

### Day 010: 2017-01-09

**Today's Progress**:

AM: Plan for the week, added my notes to a Trello board for project ideas. Played around with Atom edited this log commit in it I quite like it.

PM: Played with the [#JavaScript30](https://javascript30.com/) files, added files to my GitHub account, did the Flex Panel Gallery and the Fun With HTML5 Canvas

**Thoughts**:

Really have to take a look at the @freeCodeCamp(:fire:) Wikipedia zipline !!

Not a great deal of work [it feels like] done today!

**Up Next**:

More JavaScript30??

**Link(s) to work**:

[05 - Flex Panel Gallery](https://github.com/spences10/JavaScript30/tree/master/05%20-%20Flex%20Panel%20Gallery)

[08 - Fun with HTML5 Canvas](https://github.com/spences10/JavaScript30/tree/master/08%20-%20Fun%20with%20HTML5%20Canvas)

---

### Day 011: 2017-01-10

**Today's Progress**:

AM: Tidy my freeCodeCamp(:fire:) repo, removed/renamed files

PM: Created another Twitter bot this one themed on #Archer to quote back random archer quotes when matching keywords, I learned how to use the `requre(module-name)` to pass random strings to the bot.

**Thoughts**:

Inspired by [QuimperEmanuel](https://twitter.com/QuimperEmanuel) great Twitter bot [SuperHeroesTwitterBotCoding](https://github.com/EQuimper/MyOwnChallenge-SuperHeroesTwitterBotCoding)

**Up Next**:

More Twitter-bot!

**Link(s) to work**:

[freeCodeCamp(:fire:)](https://github.com/spences10/freeCodeCamp)

---

### Day 012: 2017-01-11

**Today's Progress**:

AM: Archer bot get random user, Completed

PM: Set up the [#301DaysOfCode](https://github.com/spences10/301-days-of-code) repo, added retweet function to archerbot

**Thoughts**:

Not sure if setting up a repo could be classed as part of my hour of code, also I have one of my repos which is personal but also work related have several PRs to it

**Up Next**:

More archerbot! Going to attempt to add [sentiment-3](https://market.mashape.com/vivekn/sentiment-3) and functionality to specific phrases. Add functionality for 'Phrasing?' :smile:

**Link(s) to work**:

[#301DaysOfCode](https://github.com/spences10/301-days-of-code)

[archer-twitter-bot](https://github.com/spences10/archer-twitter-bot)

---

### Day 013: 2017-01-12

**Today's Progress**:

AM: Added Archer Twitter bot favorite function with error handling

PM: Added Phrasing? responses and post tweet media, I need to work out how to serve html images so I can attach to tweet

**Thoughts**:

I'm learning a lot about Archer doing this :fire:

**Up Next**:

Archer bot user interaction via Twitter.stream using callbacks :scream:, posting giph relating to query string :question:

**Link(s) to work**:

[archer-twitter-bot](https://github.com/spences10/archer-twitter-bot)

---

### Day 014: 2017-01-13

**Today's Progress**: 

AM: Used the npm package how-to-npm, couldn't get past dist tagging, probably me being thick.

PM: Added 'Phrasing' replies to Archer bot, not great functionality as it just mentions user.

**Thoughts**:

**Up Next**:

Add reply to user for Phrasing with Archer bot

**Link(s) to work**:

[archer-twitter-bot](https://github.com/spences10/archer-twitter-bot)

---

### Day 015: 2017-01-14

**Today's Progress**:

AM: Looked into using [request](https://www.npmjs.com/package/request#star) on npm, got an example working `request('https://m.popkey.co/54f65e/YNzqV.gif').pipe(fs.createWriteStream('doodle.gif'));
` pretty straight forward so looking to get that working in Archer bot with replies [which aren't working]

PM: Created PR for [100DaysOfCode-twitter-bot](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot) project of teh day functionality using unique random array. Played with getting the giphy api working, not much joy so far

**Thoughts**:

**Up Next**:

**Link(s) to work**:

[archer-twitter-bot](https://github.com/spences10/archer-twitter-bot)

[project-of-the-day](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/pull/25/)

---

### Day 016: 2017-01-15

**Today's Progress**:

AM: Worked on adding what I have learned on Archer bot into my spences10 twitter bot, add error handling and more to the query strings. Went back to Archer bot managed to get Giphy api working able to save and tweet random gif but traversing the JSON to get a search result is taking a lot longer that expected. Ended up pushing the functionality to the dev branch on GitHub

**Thoughts**:

I need to stop dicking around with the Tweet-bot stuff and progress the freeCodeCamp(:fire:) curriculum, it has been a learning experience in what I don't know about [node, npm, JavaScript...]

**Up Next**:

Wikipedia viewer for FCC!!!!!!!

**Link(s) to work**:

[archer-twitter-bot](https://github.com/spences10/archer-twitter-bot)

[Twitter-McTwitbot](https://github.com/spences10/archer-twitter-bot/tree/dev)

---

### Day 017: 2017-01-16

**Today's Progress**:

AM: Read some really good node.js documentation the other night and decided to use what I had learned on my twitter bot, changing the file structure and adding Heroku environment variables instead of the config keys for the bot

PM: freeCodeCamp(:fire:) Wikipedia viewer zipline progress made

**Thoughts**:

Deployment to Heroku was smooth with minimal issues

**Up Next**:

Use the Twitchtv JSON API?? Maybe something in node.js, the Archer bot is still broken

**Link(s) to work**:

[RisingStack node-hero](https://risingstack.com/resources/node-hero)

[Twitter-McTwitbot](https://github.com/spences10/archer-twitter-bot/tree/dev)

[Wikipedia viewer on GitHub :octocat:](https://github.com/spences10/freeCodeCamp/tree/master/Wikipedia%20Viewer)

[Wikipedia viewer on CodePen](http://codepen.io/spences10/full/GrjbXe/)

---

### Day 018: 2017-01-17

**Today's Progress**:

AM: Added README for my freeCodeCamp(:fire:) repo

PM: Created twitter-bot-bootstrap for use with Node.js and `twit`

**Thoughts**:

**Up Next**:

For the bootstrap I'll need to detail the following on the README.md:
- Heroku CLI
- Heroku Procfile
- Heroku variables

**Link(s) to work**:

[spences10 freeCodeCamp(:fire:) on GitHub :octocat:](https://github.com/spences10/freeCodeCamp)

[twitter-bot-bootstrap](https://github.com/spences10/twitter-bot-bootstrap)

---

### Day 019: 2017-01-18

**Today's Progress**: 

AM: Got broken Heroku app working `worker: node index.js` in the `Procfile` in place of `worker: node bot.js` which was why it was crashing.

PM: Created a detailed README for anyone wanting to use the bootstrap, added the bootstrap to the [awesome-twitter-bots](https://github.com/amandeepmittal/awesome-twitter-bots) repo.

**Thoughts**:

Think I'm done with Twitter bots! :confused:

**Up Next**:

The freeCodeCamp(:fire:) Intermediate Algorithm Scripting or Use the Twitch.tv JSON API

**Link(s) to work**:

[twitter-bot-bootstrap](https://github.com/spences10/twitter-bot-bootstrap)

[awesome-twitter-bots](https://github.com/amandeepmittal/awesome-twitter-bots)

---

### Day 020: 2017-01-19

**Today's Progress**:

AM: Added some more detail to the README on my Twitter bot bootstrap, did one of the Intermediate Algorithm Scripting freeCodeCamp(:fire:) challenges

PM: Moar detail to the Twitter bot bootstrap README and some detail for a blog post.

**Thoughts**:

Still learning loads about Node.js and Twitter, feeling pretty burned out the last few days.

**Up Next**:

**Link(s) to work**:

[twitter-bot-bootstrap](https://github.com/spences10/twitter-bot-bootstrap)

---

### Day 021: 2017-01-20

**Today's Progress**:

AM: Learned more about callbacks in node.js with [RisingStack](https://www.youtube.com/watch?v=ca7HAqbfd90) and [Kyle Robinson Young](https://www.youtube.com/watch?v=qN0dkXj7jc0)

PM: Looked into using [level](https://github.com/Level/level)

**Thoughts**:

Not a great deal going on, Friday yo! Beer time :beers:

**Up Next**:

Going to look at some form of logging for the #100DaysOfCode Twitter bot so users aren't getting hit wil loads of tweets

**Link(s) to work**:

---

### Day 022: 2017-01-21

**Today's Progress**:

AM: Spent an hour and a half trying to work out how to use level, I'm so confused with it...

Code:

```
var db = require('./db', {
  valueEncoding: 'json'
})

db.put('name', 'ID001')
db.put('name', 'ID002')
db.put('name', 'ID003')
db.put('name', 'ID004')
db.put('name', 'ID005')
db.put('name', 'ID006')
db.put('name', 'ID006')

db.list(function(key, value) {
        console.log(key + ': ' + value);
    });
```

Terminal output:

```
spences10:~/workspace/level-db $ node app.js
value: ID006
spences10:~/workspace/level-db $ node app.js
value: ID006
spences10:~/workspace/level-db $ node app.js
value: ID006
spences10:~/workspace/level-db $ node app.js
value: ID004
spences10:~/workspace/level-db $ node app.js
value: ID006
spences10:~/workspace/level-db $ node app.js
value: ID005
spences10:~/workspace/level-db $ node app.js
value: ID006
spences10:~/workspace/level-db $ node app.js
```

WTF??

I want to be able to read the data that's in the db, I'm guessing I'm missing something really simple.

PM: Did some [Intermediate Algorithm Scripting](https://github.com/spences10/freeCodeCamp/tree/master/Intermediate%20Algorithm%20Scripting)

**Thoughts**:

Really struggling with [level](https://github.com/Level/level), something deemed really simple... don't know what I'm missing

**Up Next**:

**Link(s) to work**:

[Intermediate Algorithm Scripting](https://github.com/spences10/freeCodeCamp/tree/master/Intermediate%20Algorithm%20Scripting)

---

### Day 023: 2017-01-22

**Today's Progress**:

AM: LevelDB education continues, adjusted a commit for a PR to the 100DaysOfCode Twitter bot, learned more about using node.js

PM: Testing LevelDB, the thing which is causing problems? `if (typeof(value) !== 'undefined')` either the user is there or not so return a string value or `undefined` 

PR Submitted for 100DaysOfCode twitter bot

**Thoughts**:

WTF LevelDB! Not really, well, ok wtf Scott!!

**Up Next**:

**Link(s) to work**:

[100DoC Twitter bot PR](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot/pull/30)

---

### Day 024: 2017-01-23

**Today's Progress**:

AM: Followed along on the Node.js courses [here](https://www.youtube.com/watch?v=ioxgbkxIGwE&index=4&list=PL55RiY5tL51oGJorjEgl6NVeDbx_fO5jR) with [Maximilian](https://twitter.com/maxedapps) 

Set up a local page 'Hello World! learned more about `module.exports` good stuff

PM: Started the [freeCodeCamp(:fire:) beta site](http://beta.freecodecamp.com/en/spences10)

**Thoughts**:

Learning so much about node :+1:

**Up Next**:

More node.js videos

**Link(s) to work**:

I'll add the node.js to GitHub soon

[my freeCodeCamp(:fire:) beta site profile](http://beta.freecodecamp.com/en/spences10)

---

### Day 025: 2017-01-24

**Today's Progress**:

AM: Gawped at other users GitHub profiles :heart: [KingPixil](https://github.com/KingPixil) :heart:

PM: Followed along with more [node.js basics](https://www.youtube.com/watch?v=tiMLxUKrB-g&list=PL55RiY5tL51oGJorjEgl6NVeDbx_fO5jR&index=6)

**Thoughts**:

Tired, so, so tired

**Up Next**:

Going to take a look at my personal site

**Link(s) to work**:

[My GitHub repo](https://github.com/spences10/node-basics)

---

### Day 026: 2017-01-25

**Today's Progress**:

**Thoughts**:

**Up Next**:

**Link(s) to work**:
