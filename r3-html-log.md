**#100DaysOfCode Log - Round 3 - Anubis Lockward**
**The log of my #100DaysOfCode challenge. Started on [September 21st, Tuesday, 2021].**

## [Log Entries](#log-entries)

- [Entries for 2021](#2021)
  - [Day 006 - Latest entry](#day-006)
  - [Day 005](#day-005)
  - [Day 004](#day-004)
  - [Day 003](#day-003)
  - [Day 002](#day-002)
  - [Day 001](#day-001)

- [About me](#about-me)

### Day 001
**Round 3 Day 001, Sep 25th, 2021**
## Contents 001
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-001)
- [What I did today](#what-i-did-on-day-001)
- [Interesting links](#interesting-links-001)

## Ramblings and inner thoughts 001

I do not want to forget this feeling, this excitement of being here once again. This will be the third round of a journey that started all the way back in December 6th of 2018. It's been hard. Many obstacles in the way have let me to starting over several times. The second round took me from April 19th 2019 until yesterday to finish, having had to start over three times before finally committing full time to this. I have been highly focused on pushing forward, now learning JavaScript and Node, and many other stuff, even non related to programming. I am focusing on programming a simple online text based game and practicing more than learning new stuff. I am even learning Math on Khan Academy, started all the way from Basic Math and have been putting 30 minutes to it almost daily.

- I think I managed to fix the bug that was mixing the distances for both Gungurk and The Stone. It seems it was being caused by a global `distance` variable which I ended up eliminating, and the other thing had to do with the order of execution of the enemy, The Stone and Gungurk's actions. Apparently, I programmed the game's logic to take into account the TaintedRoot enemies taking their turns first. I have to fix this.

- Add display that shows all four enemies at once on `1a_fight` scenario.
- The display should show all four enemies above the two players.
- To add all enemies, the game will use a for loop to add each one separately.
- Should add a unique ID to each enemy.
- When players attack, they should be able to attack one of the enemies.
- The targets for the player's attack will be picked at random.
- Only a single target should be attacked by the players.
- Pick one of the random enemies to act on a turn.
- Modify code to use finite state machines with switch cases to determine the enemy's actions.
- The States should be: Pick target, if it has a target attack it, if the attack hits grapple target, if target is grappled pull it towards the chasm, alive, and dead.
- For the players, the States should be: grappled, fell, dead.
- Game logic should search for dead enemies to remove them from the game before acting on a turn.
- Adjusted size of the GUI avatars, changing it from fixed pixel size to View Port Heights and View Port Width.


## What I did on day 001

TO DO | Status | Pomodoros
----- | ------ | ---------
30 minutes of Math on Khan Academy |  |
Keep learning a bit of Node |  |
Fix bug that shows Vines as being attacked when combat starts |  |
When Gungurk falls to the Chasm, his GUI should be removed |  |
Implement a way of adding and removing GUI elements from the Display |  |

## Interesting links 001

[:arrow_double_up:](#day-001)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 002
**Round 3 Day 002, Sep 27th, 2021**
## Contents 002
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-002)
- [What I did today](#what-i-did-on-day-002)
- [Interesting links](#interesting-links-002)

## Ramblings and inner thoughts 002

There is a bug causing an infinite loop, possibly when picking a random enemy or a random target. I have to map the behaviors better

## What I did on day 002

- [X] Create an array that contains all of the entities (enemies, and allies)
- [X] Add a field to the entities that specify if they're an enemy or an ally.
- [X] When in "idle" state, the Enemy will pick a target that's an "ally"
- [ ] Selected target will not be switched until the target is defeated or the enemy is killed.
- [ ] Add idle state to the Player objects
- [ ] Allies will also select a random "Enemy" from the array of entities when in "idle" state.
- [ ] The selected "enemy" will not be switch until it is defeated.

## Interesting links 002

[:arrow_double_up:](#day-002)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 003
**Round 3 Day 003, Oct 02nd, 2021**
## Contents 003
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-003)
- [What I did today](#what-i-did-on-day-003)
- [Interesting links](#interesting-links-003)

## Ramblings and inner thoughts 003

I did something job related. I programmed an automated task using Node.js and Selenium on Windows. Have ran a couple of test and they are running just fine. I'm really happy with the result.

## What I did on day 003

- [ ] Fix bug causing infinite loop when picking random enemy or random target.
- [ ] Selected target will not be switched until the target is defeated or the enemy is killed.
- [ ] Add idle state to the Player objects
- [ ] Allies will also select a random "Enemy" from the array of entities when in "idle" state.
- [ ] The selected "enemy" will not be switch until it is defeated.

## Interesting links 003

[:arrow_double_up:](#day-003)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 004
**Round 3 Day 004, Oct 03rd, 2021**
## Contents 004
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-004)
- [What I did today](#what-i-did-on-day-004)
- [Interesting links](#interesting-links-004)

## Ramblings and inner thoughts 004

## What I did on day 004

- [X] Fix bug causing infinite loop when picking random enemy or random target.
- [X] Selected target will not be switched until the target is defeated or the enemy is killed.
- [ ] Add idle state to the Player objects
- [ ] Allies will also select a random "Enemy" from the array of entities when in "idle" state.
- [ ] The selected "enemy" will not be switch until it is defeated.

## Interesting links 004

[:arrow_double_up:](#day-004)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 005
**Round 3 Day 005, Oct 7th, 2021**
## Contents 005
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-005)
- [What I did today](#what-i-did-on-day-005)
- [Interesting links](#interesting-links-005)

## Ramblings and inner thoughts 005

- Learning about Finite State Machine to program the AI of the Entities in the Dark Awakenings game.

## What I did on day 005

- [X] Remove unused code.
- [X] When the enemy chooses a target, it should display a message indicating which target it picked.
- [X] Add idle state to the Player objects
- [X] Allies will also select a random "Enemy" from the array of entities when in "idle" state.
- [X] The selected "enemy" will not be switch until it is defeated.
- [X] Changed The Stone's behavior to work with Finite State Machine.
- [X] Changed Tainted Root's behavior to work with Finite State Machine. -This was done a few days ago-

## Interesting links 005

- [Implementing an AI with Finite State Machine in Unity](https://developpaper.com/implementing-an-ai-with-finite-state-machine-in-unity/)
- [Combat AI for Action-Adventure Games Tutorial - Unity/C# - GOAP](https://youtu.be/n6vn7d5R_2c)
- [Simple Enemy AI in JavaScript](https://youtu.be/zbqwFb8DJgQ)

[:arrow_double_up:](#day-005)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 006
**Round 3 Day 006, Oct 9th, 2021**
## Contents 006
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-006)
- [What I did today](#what-i-did-on-day-006)
- [Interesting links](#interesting-links-006)

## Ramblings and inner thoughts 006

- When The Stone breaks free from a Tainted Root's grapple, this immediately kills it, but it creates a bug when that Tainted Root was the last one remaining. The game should switch immediately to the scenario where all the enemies die but it doesn't, instead it needs another iteration where the attack button is pressed to realize that there are no more enemies. I should maybe create a function that ensures that no more enemies are remaining.

- There seem to also be some bugs where a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm.

- There also appears to be another bug where even if the Tainted Root manages to drag Gungurk into the Chasm -which kills the Tainted Root-, the Tainted Root can still be targetted, but immediately as it is picked, the game then switches the Player to "idle" mode and picks another Tainted Root.

- There is a bug that causes that a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm or was killed.

- There is another bug that causes the game to continue after The Stone was killed, which messes up everything.

## What I did on day 005

- [X] Implement Finite State Machine to handle Gungurk's behavior.
- [X] When Gungurk has the "grappled" condition, he will always attempt to escape.
- [X] If Gungurk is less than 15ft from the Chasm, he will always try to back off (if he is not grappled)

## Interesting links 006

- []()

[:arrow_double_up:](#day-006)

[Back to the beginning :arrow_double_up:](#log-entries)

## About me

- Should have to put a description in here some day. In the mean time, you are already on my [github], you can also see what is supposed to be my portfolio [website], and if you want you can see my posts on [twitter] thought I only use the platform to post updates on my coding journey.

[github]: https://github.com/mr2much
[website]: https://mr2much.github.io/webdev/
[twitter]: https://twitter.com/Cold_Dog