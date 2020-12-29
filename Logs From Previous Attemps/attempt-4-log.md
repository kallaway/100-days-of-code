# #100DaysOfCode Log - Round 4 - Clay Reber

The log for my fourth round. Started 12/16/20

## REMINDER: I WILL NEED TO ADD 1 DAY TO THIS STREAK TO MAKE UP FOR MISSED DAYS

## Log

### R4D1 (12/16/20)

Debated wether to start this again during Finals week but honestly this felt like a much needed break between tests. 

Started work on learning how to solve a Klotski puzzle (example of said puzzle here: https://www.schoolarchimedes.com/klotski). Was about to google how to make a klotski puzzle so I could start working on the solving algorithm instantly, but decided against it. This projects seems simple enough to be a prime opportunity to mess with UnitTests and TDD. 

So I spent most of the hour making basic UnitTests in Python. Now I am starting to write my first tests for the board. Current task is seeing how to check if a method exists in a project (which my tired brain just realized is a stupid thing to do).


### R4D2 (12/17/2020)

Today was really fun. It was purely a day getting reacquainted with running tests. It took so long just to figure out how to get a basic function and variable to pass the suite. But holy shit it felt good to get them to pass! TO be fair, I was only passing integers, so I know it will be eons harder to learn how to test a game board. But I can already feel the benefits of running tests before writing any code. I may have a simple function that only values a single integer, but I can tell running these tests will help compartmentalize this project into smaller chunks which will be much easier for me to handle. 

Tomorrow I plan to figure out how I intend to create the game board for Klotski. I first intended it to be just a matrix, but who knows. Maybe TDD will help me see something I'm missing. Perhaps I should focus on creating individual blocks first before I create the board? I had never thought of that until now.


### R4D3 (12/18/2020)

Aside from a few big successes, today was a big kick in the nuts at school. Almost demoralized he, but here I am. 

Continued the grueling task of TDD. It is definitely slower than if I just coded stuff out, but like I said before, it helps so much in breaking huge problems into small pieces. 

Thanks to TDD, I realized one key think I didn't think of before; I will need to have a visual environment first before I can even make the board. Unlike Sudoku, Klotski is a game with rules based on the physical dimensions of its pieces. So I can't create the computing logic of the game unless I have these rules in place. 

Decided to use the PyGame library. Its fast to import and there are a lot of tutorials on how to use it. 

So yeah. Was able to create a plane of existence I can now put my game board pieces on. UnitTest isn't working anymore, sadly, so I'm going to start tomorrow with finding out how to fix it or write new tests. 

### R4D4 (12/19/20)

Writing the hour i put in for yesterday. Was stuck in writer's block. Got frustrated with most of my code and deleted most of it. Almost gave up on TDD.

However, after such a crappy day, read this and it make me feel a lot better about my current position: https://www.freecodecamp.org/news/test-driven-development-what-it-is-and-what-it-is-not-41fa6bca02a2/. Realized I was focusing on the wrong parts of TDD, as well as not implementing it properly to begin with. Hope to change that today. 

### R4D5 (12/20/20)

I have somewhere else to be, else I would spend more than an hour on this today. 

May not have made any production code today, but I learned some very valuable lessons.
1: TDD is not a substitution for the design phase of a program. 
2: Performance tuning in the Green phase of TDD is usually premature optimization. 
3: Separate your GUI and your program logic as much as possible. 

I should have learned this by now from my capstone. Also, I switched to Tkinter as my GUI for the time being. Lets see if it works well tomorrow. 

### R4D6 (12/22/20)

Was originally going to code late last night, but opened my powershell exactly 12:00 midnight, so I felt it would have been cheating saying it would have counted. 

An awesome epiphany occurred to me today: I've already been working with GUI management and automatic tests in Flutter. I could kill two birds in one stone with this project by getting more familiar with my Capstone environment AND by having a GUI I already know how to run tests in. 

So yeah, all I pretty much did today was set up a flutter environment in this repo. Took a sec, but all the demos run perfectly. Will be changing my current coding language from python to dart. 

I SWEAR, I will have actual coding progress made tomorrow. I feel bad for not coding sooner, but I do think this will be more useful for me down the road. Besides, I'm still following the rule I learned Sunday: TDD is not a substitution for the design phase of a program.

### R4D7 (12/23/20) 

Upgrading to Flutter was a great decision. I feel so much more in my element now, and running tests is better than ever. 

The only con I feel I've gotten from switching are the overreliance of packages. I was looking for an example of chess to reference off of, since I am having trouble finding a widget which is just moving a piece around the page. But it seems to me everyone in the Flutter community just uses the exact same chess package on pub.dev and nothing else. You'd think a community as large as flutter's would have mor originality. 

I was going to code more, but I've done my hour, and I need to learn to just relax when I know I've done my part for the day. I spend so much time catching up on classes and code, it almost never feels like there's a stopping point. I also want to play Destiny rn, so whatever. 


### R4D8 (12/24/20)

To anyone who reads this, Merry Christmas Eve. 

Trying to pass my first test, which is to get the main page running XD. I could have just worked with the demo the flutter project started me with, but I want to simulate as much of my Capstone project as I can, without using a backend. So I'm making my main file very bare-bones, just the initiation and root of my application. It's definitely a lot of extra work to just past my first test, but I can at least say I am working toward making it pass. 

Today's coding feels very comfortable. It might be me just getting used to coding daily, or it could be the relieve of not spending another day deciding my development environment. I don't know, today just feels good.

Just did some more research on good coding ideas: 

 - https://www.freecodecamp.org/ (Decided to finally look at a recommendation by another Twitter user, and holy crap this is some good shit. Might do this alongside making my game, and i could start testing each challenge from the very beginning so I can slowly build up my testing skills.)
 - https://www.geeksforgeeks.org/100-days-of-code-a-complete-guide-for-beginners-and-experienced/ 
 - https://www.udemy.com/course/100-days-of-code/ (This costs money and only focuses on python so this might be a bad idea)

 Again, Merry Christmas Eve, everyone.





