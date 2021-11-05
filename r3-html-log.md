**#100DaysOfCode Log - Round 3 - Anubis Lockward**
**The log of my #100DaysOfCode challenge. Started on [September 21st, Tuesday, 2021].**

## [Log Entries](#log-entries)

- [Entries for 2021](#2021)
  - [Day 023 - Latest entry](#day-023)
  - [Day 022](#day-022)
  - [Day 021](#day-021)
  - [Day 020](#day-020)
  - [Day 019](#day-019)
  - [Day 018](#day-018)
  - [Day 017](#day-017)
  - [Day 016](#day-016)
  - [Day 015](#day-015)
  - [Day 014](#day-014)
  - [Day 013](#day-013)
  - [Day 012](#day-012)
  - [Day 011](#day-011)
  - [Day 010](#day-010)
  - [Day 009](#day-009)
  - [Day 008](#day-008)
  - [Day 007](#day-007)
  - [Day 006](#day-006)
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

## What I did on day 006

- [X] Implement Finite State Machine to handle Gungurk's behavior.
- [X] When Gungurk has the "grappled" condition, he will always attempt to escape.
- [X] If Gungurk is less than 15ft from the Chasm, he will always try to back off (if he is not grappled)

## Interesting links 006

- []()

[:arrow_double_up:](#day-006)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 007
**Round 3 Day 007, Oct 10th, 2021**
## Contents 007
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-007)
- [What I did today](#what-i-did-on-day-007)
- [Interesting links](#interesting-links-007)

## Ramblings and inner thoughts 007

- Added a few more scenarios to the first encounter. Specifically the running away options and an ending where you abandon your friends.

- On `1a_break_success.html` scenario, when the `Run Away` button is clicked, there shouldn't be a need to check if The Stone is escaping alone, since Gungurk will always be grappled in this case, so The Stone will always escape alone.

- I started learning how to separate multiple commands, or in this case, behaviors, into their own separate files to clean up the code a bit more. I think that this way I will be able to fix a few of the bugs that I have found so far.

## What I did on day 007

- [X] Removed code that checked if The Stone was in a party when he picked the **Run Away** option on `1a_break_success.html`

- [ ] Fix bug where when The Stone breaks free from a Tainted Root's grapple, this immediately kills it, but it creates a bug when that Tainted Root was the last one remaining. The game should switch immediately to the scenario where all the enemies die but it doesn't, instead it needs another iteration where the attack button is pressed to realize that there are no more enemies. I should maybe create a function that ensures that no more enemies are remaining.

- [ ] Fix bug where a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm.

- [ ] Fix bug where even if the Tainted Root manages to drag Gungurk into the Chasm -which kills the Tainted Root-, the Tainted Root can still be targetted, but immediately as it is picked, the game then switches the Player to "idle" mode and picks another Tainted Root.

- [ ] Fix bug that causes the game to continue after The Stone was killed, which messes up everything.

## Interesting links 007

- []()

[:arrow_double_up:](#day-007)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 008
**Round 3 Day 008, Oct 11th, 2021**
## Contents 008
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-008)
- [What I did today](#what-i-did-on-day-008)
- [Interesting links](#interesting-links-008)

## Ramblings and inner thoughts 008

- Working on refactoring the `1a_fight.js` code to handle the Tainted Root's behavior.

## What I did on day 008

- [ ] Separate behavior control logic for each Entity on the `1a_fight` script
      - [X] Create a folder to place all the behavioral scripts
      - [ ] Create a separate folder in that folder to handle the behaviors of the Entities.
      - [ ] Create script file to handle Dead behavior
      - [ ] Create script file to handle Idle behavior.
      - [ ] Create script file to handle Attack behavior
      - [ ] Create script file to handle Drag behavior
      - [ ] Create script file to handle Falling behavior
      - [ ] Create script file to handle Retreat behavior
      - [ ] Create script file to handle Escape behavior

- While I just started working on the things pointed above, I think I managed to solve one of the bugs where the Tainted Roots kept targetting Gungurk when he fell into the Chasm. I have not have time to test it, but I found out that the Target was being referenced by a global Tainted Root reference instead of the Tainted Root currently grappling him.

- [ ] Fix bug where when The Stone breaks free from a Tainted Root's grapple, this immediately kills it, but it creates a bug when that Tainted Root was the last one remaining. The game should switch immediately to the scenario where all the enemies die but it doesn't, instead it needs another iteration where the attack button is pressed to realize that there are no more enemies. I should maybe create a function that ensures that no more enemies are remaining.

- [ ] Fix bug where a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm.

- [ ] Fix bug where even if the Tainted Root manages to drag Gungurk into the Chasm -which kills the Tainted Root-, the Tainted Root can still be targetted, but immediately as it is picked, the game then switches the Player to "idle" mode and picks another Tainted Root.

- [ ] Fix bug that causes the game to continue after The Stone was killed, which messes up everything.

## Interesting links 008

- [javascript: modifing an imported 'variable' causes 'Assignment to constant variable' even it is not a constant](https://stackoverflow.com/questions/53723251/javascript-modifing-an-imported-variable-causes-assignment-to-constant-varia)
- []()

[:arrow_double_up:](#day-008)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 009
**Round 3 Day 009, Oct 14th, 2021**
## Contents 009
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-009)
- [What I did today](#what-i-did-on-day-009)
- [Interesting links](#interesting-links-009)

## Ramblings and inner thoughts 009

- Still working on refactoring the `1a_fight.js` to separate the code that handles the entity's behaviors.

- Since the Tainted Roots are now being handled individually, we don't need to use the pickRandomEntityOfType() function to select a new Tainted Root each time one of them dies.

- The CharGUI for Tainted Roots now displays their ID's next to their names.

## What I did on day 009

- [X] The Tainted Roots are now handled individually each with their own separate behavior.
- [ ] Separate behavior control logic for each Entity on the `1a_fight` script
      - [ ] Create a separate folder in that folder to handle the behaviors of the Entities.
      - [ ] Create script file to handle Dead behavior
      - [ ] Create script file to handle Idle behavior.
      - [ ] Create script file to handle Attack behavior
      - [ ] Create script file to handle Drag behavior
      - [ ] Create script file to handle Falling behavior
      - [ ] Create script file to handle Retreat behavior
      - [ ] Create script file to handle Escape behavior
- [ ] Test if the bug that allowed Gungurk to keep bieng targetted when he fell into the Chasm was fixed.

- [ ] Fix bug where when The Stone breaks free from a Tainted Root's grapple, this immediately kills it, but it creates a bug when that Tainted Root was the last one remaining. The game should switch immediately to the scenario where all the enemies die but it doesn't, instead it needs another iteration where the attack button is pressed to realize that there are no more enemies. I should maybe create a function that ensures that no more enemies are remaining.

- [ ] Fix bug where a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm.

- [ ] Fix bug where even if the Tainted Root manages to drag Gungurk into the Chasm -which kills the Tainted Root-, the Tainted Root can still be targetted, but immediately as it is picked, the game then switches the Player to "idle" mode and picks another Tainted Root.

- [ ] Fix bug that causes the game to continue after The Stone was killed, which messes up everything.

## Interesting links 009

- []()

[:arrow_double_up:](#day-009)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 010
**Round 3 Day 010, Oct 15th, 2021**
## Contents 010
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-010)
- [What I did today](#what-i-did-on-day-010)
- [Interesting links](#interesting-links-010)

## Ramblings and inner thoughts 010

- Third day of working on refactoring the `1a_fight.js` to separate the code that handles the entity's behaviors.

- I think that I finally managed to solve the bugs that caused to target dead Tainted Roots or Gungurk once he was dropped down the Chasm or killed. I have to run a few more test to confirm it.

- Right now, all of the Tainted Roots are attacking at different targets at the same time, which causes that sometimes all of them gang up on a single target, when this happens, only one of them is able to grapple the target.

- I removed the code that caused a target to get pulled and damaged when attempting to break free of a grapple and they failed, since they already wasted a turn trying to escape anyways.

## What I did on day 010

- [ ] Separate behavior control logic for each Entity on the `1a_fight` script
      - [ ] Create a separate folder in that folder to handle the behaviors of the Entities.
      - [ ] Create script file to handle Dead behavior
      - [ ] Create script file to handle Idle behavior.
      - [ ] Create script file to handle Attack behavior
      - [ ] Create script file to handle Drag behavior
      - [ ] Create script file to handle Falling behavior
      - [ ] Create script file to handle Retreat behavior
      - [ ] Create script file to handle Escape behavior

- [ ] Fix bug where when The Stone breaks free from a Tainted Root's grapple, this immediately kills it, but it creates a bug when that Tainted Root was the last one remaining. The game should switch immediately to the scenario where all the enemies die but it doesn't, instead it needs another iteration where the attack button is pressed to realize that there are no more enemies. I should maybe create a function that ensures that no more enemies are remaining.

- [ ] Fix bug where a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm.

- [ ] Test if the bug that allowed Gungurk to keep bieng targetted when he fell into the Chasm was fixed.

- [ ] Fix bug where even if the Tainted Root manages to drag Gungurk into the Chasm -which kills the Tainted Root-, the Tainted Root can still be targetted, but immediately as it is picked, the game then switches the Player to "idle" mode and picks another Tainted Root.

- [ ] Fix bug that causes the game to continue after The Stone was killed, which messes up everything.

## Interesting links 010

- []()

[:arrow_double_up:](#day-010)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 011
**Round 3 Day 011, Oct 18th, 2021**
## Contents 011
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-011)
- [What I did today](#what-i-did-on-day-011)
- [Interesting links](#interesting-links-011)

## Ramblings and inner thoughts 011

- Fourth consecutive day, still working on refactoring the `1a_fight.js` to separate the code that handles the entity's behaviors.

- Cleaned a bunch of code, removing comments and old code that was no longer needed.

- The Dead, Idle, Attack, and Drag behaviors are working fine for the Tainted Root each on their separate files.

- Moved The Stone's behavior to its own separate file. The Idle, Attack, Dead and Falling behaviors are working fine each on their own separate files.

- Moved Gungurk's behavior to its own separate file. The Dead, Idle, Attack, Escape, Falling, and Retreat behaviors are working fine each on their own separate files.

## What I did on day 011

- [X] Separate behavior control logic for each Entity on the `1a_fight` script
      - [X] Create a separate folder in that folder to handle the behaviors of the Entities.
      - [X] Create script file to handle Dead behavior
      - [X] Create script file to handle Idle behavior.
      - [X] Create script file to handle Attack behavior
      - [X] Create script file to handle Drag behavior
      - [X] Create script file to handle Falling behavior
      - [X] Create script file to handle Retreat behavior
      - [X] Create script file to handle Escape behavior

- [X] Fix bug where when The Stone breaks free from a Tainted Root's grapple, this immediately kills it, but it creates a bug when that Tainted Root was the last one remaining. The game should switch immediately to the scenario where all the enemies die but it doesn't, instead it needs another iteration where the attack button is pressed to realize that there are no more enemies. I should maybe create a function that ensures that no more enemies are remaining.

- [X] Fix bug where a Tainted Root keeps targetting Gungurk after he's been pulled into the Chasm.

- [X] Test if the bug that allowed Gungurk to keep bieng targetted when he fell into the Chasm was fixed.

- [X] Fix bug where even if the Tainted Root manages to drag Gungurk into the Chasm -which kills the Tainted Root-, the Tainted Root can still be targetted, but immediately as it is picked, the game then switches the Player to "idle" mode and picks another Tainted Root.

- [X] Fix bug that causes the game to continue after The Stone was killed, which messes up everything.

## Interesting links 011

- []()

[:arrow_double_up:](#day-011)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 012
**Round 3 Day 012, Oct 19th, 2021**
## Contents 012
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-012)
- [What I did today](#what-i-did-on-day-012)
- [Interesting links](#interesting-links-012)

## Ramblings and inner thoughts 012

- Today I found a bug that had been lurking around in the code from the beginning, which was caused because I was using `setInterval()` instead of `setTimeout()`

## What I did on day 012

- [X] The game loads two death scenarios depending on how you died.
  - [X] It loads an scenario when you die due to damage.
  - [X] It loads an scenario when you die due to falling into the chasm.

## Interesting links 012

- []()

[:arrow_double_up:](#day-012)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 013
**Round 3 Day 013, Oct 20th, 2021**
## Contents 013
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-013)
- [What I did today](#what-i-did-on-day-013)
- [Interesting links](#interesting-links-013)

## Ramblings and inner thoughts 013

- Today I decided to work more on the narrative aspect of the game since mechanically it is more polished. Also noticing where some of the behavior handlers could be reused in the game. Thought for that I'd have to refine the behavior handlers a bit more and get them out from where I put them which is the `1a_fight` scenario.

- Added a couple more text to some scenarios.

- Added a few more branches of choices.

- Added a few more bugs, which I then promptly corrected.

## What I did on day 013

- [X] Separate GameObject behavior into own separate file.

- [X] Removed unnecessary code form `choices.js`

- [X] Implemented a few more missing scenarios on the game.

## Interesting links 013

- []()

[:arrow_double_up:](#day-013)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 014
**Round 3 Day 014, Oct 23rd, 2021**
## Contents 014
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-014)
- [What I did today](#what-i-did-on-day-014)
- [Interesting links](#interesting-links-014)

## Ramblings and inner thoughts 014

- I found and fixed a bug that sneaked on me as I was refactoring the `intro_choices` script which was messing up the amount of enemies you were fighting against on the `1a_fight` scenario.

- Also kept adding more narrative and new scenarios to the game. I think I'm nearly completing the first encounter.

- I found out that the behaviors of the Entities are too tightly coupled to the `1a_fight` script, which is causing that I cannot use them as separated pieces of code. Apparently the bug is being caused by the event listener on window object.

- I have to refactor getDistanceForCharacter and the distanceFromChasm object, so that the value is stored in the character object instead of the game object so that I don't have to pass a reference to the gameObject on the character's behavior handler.

## What I did on day 014

- [X] Move the Escape Behavior for The Stone to its own separate file.
- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Set the grappledBy property on The Stone's reference to the Tainted Root so that The Stone is able to run Escape on it
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Using The Stone's behavior handler, I should invoke the Escape behavior
- [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
- [ ] On `2a_look` option two should take you to `1a_break_success`
- [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.


## Interesting links 014

- []()

[:arrow_double_up:](#day-014)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 015
**Round 3 Day 015, Oct 24th, 2021**
## Contents 015
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-015)
- [What I did today](#what-i-did-on-day-015)
- [Interesting links](#interesting-links-015)

## Ramblings and inner thoughts 015

- Today I'm going to work on turning the behavior handler into a class of its own and make the behavior handlers of the entities subclasses of it.

- Today I turned the `notifyObservers` function into its own object called ObserverHandler.

- Removed `enemyDied` function from `1a_fight` script and moved the code that was there to the `dead` state of the Tainted Root. Also removed the use of the `amountOfEnemies` variable since I'm going to implement at some point a way of removing the GUI elements when an entity is killed.

- Should I maybe modify the combat scenario on `1a_fight` so that the fight runs on its own immediately as you click the **Attack** button?, or should I keep it running as is, one click at a time?, right now this is causing some issues because the behaviors of the entities are not being immediately executed when they change, they always need at least one more iteration before the game refreshes the new behavior.

- The code on `1a_fight` now has a strange bug that is causing that I have to click two or three times for it to update the states of the entities. Which is caused by the removal of the `enemyDied` function from the `1a_fight` script. What that function basically did was immediately run the dead behavior of the TaintedRoot and immediately updated the count and removed the entities.

- I'm not sure if I should keep the reference to the GameObject when handling the behaviors of the entities.

## What I did on day 015

- [X] Placed all of the Entities in an Entity container on a separate file and remove it from `1a_fight`. I am using this Entity Container to know how many enemies remain as well as remove the entities that died from the container.

- [X] The ObserverHandler class should have a method to add, notify, and remove observers.
  - [X] Implement method to add observers.
  - [X] Implement method to notify observers.
  - [X] Implement method to remove observers.
  - [X] Replace all references to notifyObservers anywhere they appear so that they use the ObserverHandler
    - [x] Replace references to notifyObservers so that they use the ObserverHandler in `1a_fight`
    - [x] Replace references to notifyObservers so that they use the ObserverHandler in `2a_hackvine`
    - [X] Replace references to notifyObservers so that they use the ObserverHandler in `1a_help_axe`

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Set the grappledBy property on The Stone's reference to the Tainted Root so that The Stone is able to run Escape on it
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Using The Stone's behavior handler, I should invoke the Escape behavior
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.


## Interesting links 015

- []()

[:arrow_double_up:](#day-015)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 016
**Round 3 Day 016, Oct 25th, 2021**
## Contents 016
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-016)
- [What I did today](#what-i-did-on-day-016)
- [Interesting links](#interesting-links-016)

## Ramblings and inner thoughts 016

- The Behavior Handler now has an array with all of the entities currently in game separated by type, "hostiles" or "ally"; which helps the entities for targetting on combat scenarios. It also has other functions like adding, removing and counting entities either by type, or by total entities stored.

- I also turned the Behavior Handler into an observer.

- ObserverHandler now notifies observers using a `_notify` function which should be implemented inside of the observer. There, the observer only takes the value that interest it or monitors the entities it is interested in.

- Reincorporated the `amountOfEnemies` variable because right now I still need to rely on the amount of enemies remaining to determine when the game should move to the next scenario.

- Solved the issues that were causing the delay when updating the enemy count and the displaying of messages when the enemies died. This does not happen with Gungurk, for example, because his behavior is always the last one to run.

- I should probably eventually implement a function that doesn't rely on execution time. Right now, I am using a function that runs every `0.5 seconds` to check if the amount of enemies has changed, and update accordingly, will also change this to simply rely on the ObserverHandler, passing a reference of `this` to make the `1a_script` into an observer as well.

- Little by little am making the entities and behavior more independent from each other. I'm pretty sure that eventually I'll be able to remove the GameObject reference, and that this reference alone will be able to handle the entire game, as it should be.

- I found a glitch that only ocurred once when taking a different path to the `2a_hackvine` scenario, which killed three enemies instead of two. I'll be working on replicating this.

## What I did on day 016

- [X] Solved the problem with the code on `1a_fight` that was causing the strange bug that made necessary clicking up to three times for it to update the states of the entities.

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [X] Set the grappledBy property on The Stone's reference to the Tainted Root so that The Stone is able to run Escape on it
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [X] Using The Stone's behavior handler, I should invoke the Escape behavior
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 016

- []()

[:arrow_double_up:](#day-016)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 017
**Round 3 Day 017, Oct 27th, 2021**
## Contents 017
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-017)
- [What I did today](#what-i-did-on-day-017)
- [Interesting links](#interesting-links-017)

## Ramblings and inner thoughts 017

- Managed to kind of turn the `1a_script` into an Observer, but not by passing a reference to `this` or none of that. I just simply created a new Observer that only cares about a specific Entity, and I created it inside of the `1a_fight` script. So far it's working as intended.

## What I did on day 017

- [X] Fix glitch that only ocurred once when taking a different path to the `2a_hackvine` scenario, which killed three enemies instead of two. I'll be working on replicating this. This was also happening when you went the `1a_punch` branch.

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 017

- []()

[:arrow_double_up:](#day-017)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 018
**Round 3 Day 018, Oct 28th, 2021**
## Contents 018
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-018)
- [What I did today](#what-i-did-on-day-018)
- [Interesting links](#interesting-links-018)

## Ramblings and inner thoughts 018

- Been having a lot of fun following tutorials on the Coding Train and learning about P5. This truly reminds me of when I started learning to program many years ago. I don't even have any idea of how much time I spent today creating fun projects.

## What I did on day 018

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 018

- [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw)

- **With all of these, you should click the mouse and drag it around the screen**
- [Bubbles with Images](https://editor.p5js.org/mr2much/full/shaQM6CZ3)
- [Bubbles Intersecting 2](https://editor.p5js.org/mr2much/full/6HvX5gxreU)

- **For Bubble Popper 2 and 3, you can click on the bubbles to make them pop**
- [Bubble Popper 3](https://editor.p5js.org/mr2much/full/tr_5dfMdx)
- [Bubble Popper 2](https://editor.p5js.org/mr2much/full/M0g8CPpRQ)

- **Randomly click mouse around to create bubbles
- [Bubble Popper](https://editor.p5js.org/mr2much/full/c8fPjdxYn)
- [Bubble Storm - Hint: Right click on any location within the screen](https://editor.p5js.org/mr2much/full/c8fPjdxYn)

- [Bouncing Ball](https://editor.p5js.org/mr2much/full/yHdjQADNf)

[:arrow_double_up:](#day-018)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 019
**Round 3 Day 019, Oct 29th, 2021**
## Contents 019
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-019)
- [What I did today](#what-i-did-on-day-019)
- [Interesting links](#interesting-links-019)

## Ramblings and inner thoughts 019

- Started the Working with Data and API's in JavaScript course on the Coding Train channel.

- Did a simple example of how to use `fetch()` to pull an image from a local resource and how to display it on the DOM.

## What I did on day 019

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 019

- []()

[:arrow_double_up:](#day-019)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 020
**Round 3 Day 020, Nov 1st, 2021**
## Contents 020
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-020)
- [What I did today](#what-i-did-on-day-020)
- [Interesting links](#interesting-links-020)

## Ramblings and inner thoughts 020

- Continuing on with the Data and API's in JavaScript course on the Coding Train channel.

## What I did on day 020

- [X] Loaded CSV file from NASA's GISS Surface Temperature Analysis.
- [X] Manually parsed the data to read year and global temperature.
- [X] Loaded Chart.js library from CDN.
- [X] Created HTML5 Canvas element.
- [X] Styled chart on JS file.
- [X] Refactored code that loaded and parsed CSV data to work with Chart.js chart.

- [X] Did exercise 1 of the `fetch()` video of Working with Data & API's in Javascript where you have to load and show multiple images.
- [X] Did a minor refactoring to exercise 1 to make the `insertImage` function use `document.body.appendChild()`

- [X] Did exercise 2 of the `fetch()` video of Working with Data & API's in Javascript where you have to load a text file and show it on a paragraph element on the DOM.

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 020

- [NASA's GISS Surface Temperature Analysis](https://data.giss.nasa.gov/gistemp/)

[:arrow_double_up:](#day-020)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 021
**Round 3 Day 021, Nov 2nd, 2021**
## Contents 021
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-021)
- [What I did today](#what-i-did-on-day-021)
- [Interesting links](#interesting-links-021)

## Ramblings and inner thoughts 021

- Worked on exercise 2 of the Module 2 of the Working with Data & API's in JavaScript mini course from Coding Train. 

## What I did on day 021

- [ ] Create table on the page to display the reported ATM's
- [ ] Add several entries with dummy data to test the entries on the table.
- [ ] Create a class in the CSS file to highlight duplicated entries.
- [ ] Test site with real data from the report file.
  - [ ] Test with dummy file.
  - [ ] Test with real data.

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 021

- [NASA's GISS Surface Temperature Analysis](https://data.giss.nasa.gov/gistemp/)

[:arrow_double_up:](#day-021)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 022
**Round 3 Day 022, Nov 2nd, 2021**
## Contents 022
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-022)
- [What I did today](#what-i-did-on-day-022)
- [Interesting links](#interesting-links-022)

## Ramblings and inner thoughts 022

- Completed third exercise about loading and displaying two more line charts showing the temperature for the Northern and Southern Hemispheres alongside the global temperature. It is pretty interesting to notice that the global temperature is rising, and it shows a similar pattern on the Northern Hemisphere, yet on the Southern Hemisphere it seems to be dropping, while at some points in the past the temperature was higher on the Southern than in the Northern which is what I would have expected. Could it maybe due to me not being able to interpret the numbers? :thinking: would probably have to investigate a little bit more into this.

## What I did on day 022

- [ ] Create table on the page to display the reported ATM's
- [ ] Add several entries with dummy data to test the entries on the table.
- [ ] Create a class in the CSS file to highlight duplicated entries.
- [ ] Test site with real data from the report file.
  - [ ] Test with dummy file.
  - [ ] Test with real data.

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 022

- [NASA's GISS Surface Temperature Analysis](https://data.giss.nasa.gov/gistemp/)

[:arrow_double_up:](#day-022)

[Back to the beginning :arrow_double_up:](#log-entries)

### Day 023
**Round 3 Day 023, Nov 4th, 2021**
## Contents 023
- [Ramblings and inner thoughts](#ramblings-and-inner-thoughts-023)
- [What I did today](#what-i-did-on-day-023)
- [Interesting links](#interesting-links-023)

## Ramblings and inner thoughts 023

- Completed exercise 2 of module two, where I graphed a different dataset. In this instance I used a CSV file from the World Bank with the Anual GDP Growth Percentage Per Country from 1961 to 2020.

## What I did on day 023

- [X] Read the file
- [X] Extract the headers
- [X] Extract the years
- [X] Extract the country names and country codes
- [X] Extract the values for the GDP per year, on the instances where the values were empty I added zeroes as "0.00"
- [X] Displayed the data on a line graph, picking various countries.

- [ ] Create table on the page to display the reported ATM's
- [ ] Add several entries with dummy data to test the entries on the table.
- [ ] Create a class in the CSS file to highlight duplicated entries.
- [ ] Test site with real data from the report file.
  - [ ] Test with dummy file.
  - [ ] Test with real data.

- [ ] Invoke the Escape Behavior from outside when it is needed.
  - [ ] When you click the option to *Try to break from the vines* on `2a_look` an athletics contest should happen between The Stone and the vine, similar to how it happens at the start of the game.
  - [ ] On `2a_look` I should get one of the Tainted Roots, the one wrapped around Gungurk
  - [ ] Have a variable for The Stone
  - [ ] Have a reference to The Stone's behavior handler on `2a_look`
  - [ ] Once you break Gungurk free, the game should move to `1a_escape_success` scenario.
  - [ ] On `2a_look` option two should take you to `1a_break_success`
  - [ ] In the `1a_punch` scenario, you should be able to use a Strength Check to "break" the vine and free Gungurk.

## Interesting links 023

-[]()

[:arrow_double_up:](#day-023)

[Back to the beginning :arrow_double_up:](#log-entries)

## About me

- Should have to put a description in here some day. In the mean time, you are already on my [github], you can also see what is supposed to be my portfolio [website], and if you want you can see my posts on [twitter] thought I only use the platform to post updates on my coding journey.

[github]: https://github.com/mr2much
[website]: https://mr2much.github.io/webdev/
[twitter]: https://twitter.com/Cold_Dog