# #100DaysOfCode Log - Round 4 - Clay Reber

The log for my fourth round. Started 12/16/20

## Log

### R4D1 (12/16/20)

Debated wether to start this again during Finals week but honestly this felt like a much needed break between tests. 

Started work on learning how to solve a Klotski puzzle (example of said puzzle here: https://www.schoolarchimedes.com/klotski). Was about to google how to make a klotski puzzle so I could start working on the solving algorithim instantly, but decided against it. This projects seems simple enough to be a prime opportunity to mess with UnitTests and TDD. 

So I spent most of the hour making basic UnitTests in Python. Now I am starting to write my first tests for the board. Current task is seeing how to check if a method exists in a project (which my tired brain just realized is a stupid thing to do).


### R4D2 (12/17/2020)

Today was really fun. It was purely a day getting reaquanted with running tests. It took so long just to figure out how to get a basic function and variable to pass the suite. But holy shit it felt good to get them to pass! TO be fair, I was only passing integers, so I know it will be eons harder to learn how to test a game board. But I can already feel the benefits of running tests before writing any code. I may have a simple function that only values a single integer, but I can tell running these tests will help compartmentalize this project into smaller chunks which will be much easier for me to handle. 

Tomorrow I plan to figure out how I intend to create the game board for Klotski. I first intended it to be just a matrix, but who knows. Maybe TDD will help me see something I'm missing. Perhaps I should focus on creating individual blocks first before I create the board? I had never thought of that until now.


### R4D3 (12/18/2020)

Aside from a few big successes, today was a big kick in the nuts at school. Almost demoralized he, but here I am. 

Continued the grueling task of TDD. It is definitely slower than if I just coded stuff out, but like I said before, it helps so much in breaking huge problems into small pieces. 

Thanks to TDD, I realized one key think I didn't think of before; I will need to have a visual environment first before I can even make the board. Unlike Sudoku, Klotski is a game with rules based on the physical dimensions of its pieces. So I can't create the computing logic of the game unless I have these rules in place. 

Decided to use the pygame library. Its fast to import and there are a lot of tutorials on how to use it. 

So yeah. Was able to create a plane of existence I can now put my game board pieces on. UnitTest isnt working anymore, sadly, so I'm going to start tomorrow with finding out how to fix it or write new tests. 
<<<<<<< HEAD

### R4D4 (12/19/20)

Writing the hour i put in for yesterday. Was stuck in writer's block. Got frustrated with most of my code and deleted most of it. Almost gave up on TDD.

However, after such a crappy day, read this and it make me feel a lot better about my current position: https://www.freecodecamp.org/news/test-driven-development-what-it-is-and-what-it-is-not-41fa6bca02a2/. Realized I was focusing on the wrong parts of TDD, as well as not implementing it properly to begin with. Hope to change that today. 

=======
>>>>>>> 2bf6b047a7284150f2cba3f2747420387edf750b
### R4D5 (12/20/20)

I have somewhere else to be, else I would spend more than an hour on this today. 

May not have made any production code today, but I learned some very valuable lessons.
1: TDD is not a substitution for the design phase of a program. 
2: Performance tuning in the Green phase of TDD is usually premature optimization. 
3: Separate your GUI and your program logic as much as possible. 

I should have lerned this by now from my capstone. Also, I switched to tkinter as my GUI for the time being. Lets see if it works well tomorrow. 