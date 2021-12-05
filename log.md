# 100 Days Of Code - Log

### Day 4: December 5, 2021

**Today's Progress**: Today, I kept on watching "Dart Programming in 4 hours | Full beginners tutorial" on youtube from Mike Dane.

**Learned**:

1.  If and if/else statements:

```
  if(condition){ 
    action 
  }
```

```
  if(condition){ 
    action 
  } else if () { 
    action 
  }
```

2. Operators:

```
+⇒ add
- ⇒ subtract
* ⇒ multiply
/ ⇒ divide
% ⇒ modular ⇒ 10 % 3 = 1 ⇒ 3 goes into 10 3 times, and 1 is left
&& ⇒ and
|| ⇒ or
! => negation => turns true into false, and the other way around.
```

3. Comparison Operators:

```
== ⇒ equal to
!= ⇒ not equal to
< ⇒ less than
<= ⇒ less than or equal to
> ⇒ bigger than
> = ⇒ bigger than or equal to
```

**Thoughts**: Going through the basics makes me realize how much I have learned over the last few years. So many concepts and words were just not relatable and so far from what I knew initially. It's super motivating because I can see that I have moved forward, and I get excited to expand my knowledge.

### Day 3: December 4, 2021

**Today's Progress**: I moved on with watching "Dart Programming in 4 hours | Full beginners tutorial" on youtube from Mike Dane.

**Learned**:

1. Lists (called arrays in PHP): We specify what types are stored in the list by writing `<type>` after the list keyword.
   List<int> numbers = [44, 55, 4, 32];
2. Access List items with bracetnotation:
   print(numbers[0]); //44
3. Functions: Is a collection of code that can be use multiple times.
   void funcName(){} // do not return anything
4. Entrypoint of a program is the main function
   void main(){}
5. Arguments: Information that a function needs to execute.
   void funcName(String username, int age){
   print("Hi ${username}, you are ${age}");
   }
6. Return statements: We can use the keyword return in a function to give some specific information back. This information can be stored in a variable, be printed to the console, or used within another function.
7. We need to specify what type of information a function returns: int, double, String, List<int> or Map.

**Thoughts**: Arrays are called lists in Dart. Because Dart is strictly typed, it makes me wonder if there is any way to return mixed types or have arguments that are of mixed type?! But I guess not - otherwise, it wouldn't be strict, right?! :)

### Day 2: December 3, 2021

**Today's Progress**:
Got to interact with user input in the terminal and read a lot about "Sound null safty".

**Learned**:

1. To read user input in the terminal - with stdin.readLineSync();
2. Importing statements:
   import "dart:io";
3. "Sound null safety": You explicitly have to say that a variable can be null if you want it to be null, and because Dart's null safety is sound (stable), the compiler is also optimized.

**Thoughts**: Null safety seems handy, but I think I have to dig a bit deeper into the topic to understand the fact that Dart’s null safety is sound.

**Links**:
[Dart Programming in 4 hours | Full beginners tutorial](https://www.youtube.com/watch?v=5xlVP04905w)

[Null safety](https://dart.dev/null-safety)

[Artikel about Null safety](https://www.infoworld.com/article/3562572/google-dart-gains-sound-null-safety.html)

[Artikel about Null safety in German](https://tech-de.netlify.app/articles/de513466/index.html)

[Video about Null safety](https://www.youtube.com/watch?v=iYhOU9AuaFs)

### Day 1: December 2, 2021

**Today's Progress**: I started to watch "Dart Programming in 4 hours | Full beginners tutorial" on youtube from Mike Dane.

**Learned**:

1. Print statement: print("Hello World!").
2. Execution flow of the program - From top to bottom
3. Variables: Containers that can store values.
4. Strings
5. Stringinterpolation - Insert a variable into a string: "Hello ${varName}"
6. Numbers: integer (10) and doubles (10,80)
7. Booleans: can be true or false
8. Comments: //
9. The length of a String is always one more than the last index position. Example:
   String greeting = "Hello"; //has indexes 01234
   print(greeting.length); //will print 5
   print(greeting[0]); //will print H
10. Concatination: varName + varName

Example Variables:
String firstName = "Mallle";
int age = 32;
double height = 1,72;
bool isHappy = true;

**Thoughts**:
Variables need a type - unlike in javascript. So need to get more consistent in that regard.

**Links**:
[Dart Programming in 4 hours | Full beginners tutorial](https://www.youtube.com/watch?v=5xlVP04905w)

### Day 0: December 1, 2021

**Today's Progress**:
Forked the 100daysofcode repo, watched the introduction to what Flutter is and why to use Flutter.

**Learned**:

1. Flutter uses Dart.
2. Flutter has a simple and flexible layout system that was inspired by the web and includes: Row, Column, Stack, Padding, and Center.
3. Flutter is Open Source, and you can dig into the code and see how the Flutter team implemented different widgets.
4. Flutter offers you one codebase for iOs, Android, Web, and Desktop.
5. Flutter has implemented Hot Reload - means the screen will update within fractions of a second after saving the code.

**Thoughts**:
Looking forward to writing the first lines of code and digging deeper into Dart and Flutter. It might be helpful to learn more about Dart before continuing with Flutter, as Flutter uses Dart.

**Link to work**:
[100 days of code](https://www.100daysofcode.com/)
[Introduction to Flutter Development Using Dart](https://www.appbrewery.co/p/intro-to-flutter)
