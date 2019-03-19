# 100 Days Of Code - Log

### Day 1: 13 March 2019

**Today's Progress**: Forked git repo, set up SSH keys for Github, created local clone of repo, and updated this file from local. Created new repo for ruby-shapes and tried to recreate an exercise I did almost a month ago from memory. 

**Thoughts:** Some aprehension about committing to 100 days of code. Looking forward to the challenge. Got sucked in and spent a leetle bit more than 1 hour on the challenge today. 

**Link(s) to work:** [Ruby Shapes](https://github.com/sallybaker/ruby-shapes)

### Day 2: 14 March 2019

**Today's Progress**: Created new repo and cloned locally. Began working on a Ruby text adventure game. Have pushed today's work to Github. 

**Thoughts**: One hour goes by too fast. Game is currently sitting at 67 lines - many of them comments. I think part of this challenge is working out how much coding is achievable in one hour. 

**Link(s) to work**: [Ruby Adventure Game](https://github.com/sallybaker/ruby-pub-adventure)

### Day 3: 15 March 2019 

**Today's Progress**: Continued work on pub adventure game. Have pushed update to Github. 

**Thoughts** Game is currently sitting at 171 lines. I've started using the 'TODO:' tag in comments where I know I need to do more, or want to add a new feature so I can come back to it later. There's plenty of things that don't work properly at the moment as the top down approach means adding high level features and then filling in the details, thus the "TODO:" tag so I know where to come back to tomorrow. Lot's of details still to be written. 

**Link(s) to work** [Ruby Adventure Game](https://github.com/sallybaker/ruby-pub-adventure)

### Day 4: 16 March 2019

**Today's Progress**: Continued work on pub adventure game. Mostly Working on the intro logic, terminal formatting, and 's - search' logic. Have added 'junk.rb file.' Have pushed update to Github.

**Thoughts** 
- Game is currently sitting at 179 lines.  
- Spent some time setting up formatting to increase usability - spaces and lines break up the page by stages and has improved readability of the game when testing
- Don't try and use a += on a variable with a zero value 
- When developing while loops it can be helpful include a 'break' just before the end of the while loop so you're only testing one iteration in the early stages and there's no fear of an infinite loop
- Using a junk file to store code that I might want to use later but isn't working right now rather than commenting out blocks of code keeps the main file clean, readable and working 
- Re-writing strings that don't make sense in the current game logic is easier than re-writing game logic that currently works so that the current strings make sense
- Fixed a bug with the pub_description method I hadn't noticed until now - it was calling a sample pub_name rather than the current_pub so the user output was not what I intended it to be.
- Noticing a tendency to want to remove a feature if I can't get it working straight away so constant reminder to self: "Don't remove it, let's figure this out..." 

**Link(s) to work** [Ruby Adventure Game](https://github.com/sallybaker/ruby-pub-adventure)

### Day 5: 17 March 2019 

**Today's Progress**: Continued work on pub adventure game. Have pushed update to Github. 

**Thoughts** 
- Game is currently sitting at 204 lines
- The obvious answer is not always the most efficient. When randomising players, I began by creating a method to replace user prompt. Then during testing realised I could remove the method and the function call by simply declaring the variable at the beginning of the game.
- Added a "c - count friends" action yesterday and now that doens't make sense to me. Leaving it there for now while I try and remember. 
- Discovered bug with pub count when moving. Was using += in counts for pubs and drinks thinking it would increment by one. That's not what it does. Fixed errors. Reminded of Princess Bride quote: "I do not think it means what you think it means."
- Noticed the pub busy option changes with each turn if you're drinking multiple drinks in the same pub. Decided this makes logical sense and is not a bug. 
- Treasure array had punctuation that didn't work with the logic
- Added a wallet feature so now you can only buy drinks if you have enough money. Want to extend the treasure feature to add money to wallet if money is found. 
- Need to investigate if there's a pause feature in ruby to improve game flow. 
- As I'm both product owner and developer, noticing I have a tendency to start changing code before thinking through the full ramifications and best design. Expect this is natural for new developers and have started to dot point ideas in a text file before changing code to help work out if new variables are required, whether they need to be declared up front or within methods, What, if any dependencies exist between new changes and current code so they can be addressed. 
- At this stage it's still very easy to think of new features to add - not so easy to decide what to work on. As long as game isn't throwing errors as that gets fixed first. 

**Link(s) to work** [Ruby Adventure Game](https://github.com/sallybaker/ruby-pub-adventure)

### Day 6: 18 March 2019 

**Today's Progress**: Continued work on pub adventure game. Have pushed update to Github. 
- Added 'the end' ending to catch unknown user flows 
- Added "stats" action
- Added "help" action 
- Notice drink_costs always $10 when I want it to change for each pub. Fixed
- Add "look" action 
- Added a catchall option for invalid actions
- Apparently you can play with zero friends. Hmmm... 
changed: players = rand(6) to: players = rand(5) + 1
- Added prompt for drink preference and updated code where required
- Added random rounds of shots 

**Thoughts** 
- Game is currently sitting at 231 lines
- At this stage it is very easy to get bogged down in details
- When testing random options - it makes it easier to use a high chance value to trigger condition then edit the chance value when you're happy with the logic 
- Today's hour went really quick 

**Link(s) to work** [Ruby Adventure Game](https://github.com/sallybaker/ruby-pub-adventure)

### Day 7: 19 March 2019

**Today's Progress**: Working through the GitHub Learning Lab courses

**Thoughts** Although I was already familiar with the concepts of Git from using Bitbucket & Sourcetree in the past as well as recently using the basic features of GitHub to store repos for this #100DaysOfCode challenge. The GitHub Learning Lab courses provide the opportunity to revise what I already know and learn the practical application of familiar concepts like Code Review and Merge conflicts. 

**Link(s) to work** 
- [github-slideshow](https://github.com/sallybaker/github-slideshow)
- [markdown-portfolio](https://github.com/sallybaker/markdown-portfolio)
- [github-upload](https://github.com/sallybaker/github-upload)
- [github-pages-with-jekyll](https://github.com/sallybaker/github-pages-with-jekyll)
- [reviewing-a-pull-request](https://github.com/sallybaker/reviewing-a-pull-request)
- [merge-conflict](https://github.com/sallybaker/merge-conflict)

