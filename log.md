# 100 Days Of Code - Log

### Day 8: December 9, 2021

**Today's Progress**: I started the youtube track "Dart - from Novice to Expert" from Flutterly. I watched the first two videos.

**Learned**: 
1.  Static type check => happens while writing code when Dart tries to compile your code. If your code isn't type-safe, your editor will show an error. And should prevent the Developer from writing the wrong types. 
2. Run time check => an extra assessment that happens when the program is running.
4. Sound type system: Dart won't allow the code to run into an undefined state. 
3. Dynamic types. Dart won't perform type checks on dynamic types. You will have to do this yourself to avoid an exception at runtime. But at runtime Dart will infer what type the data is. 
```
dynamic age = 33;
```
4. Type Inference: Types don't need to be annotated because Dart can statically infer the type. We just need to use the keyword var. Dart does this by using the static type analyzer, which I learned about in the first step. 
```
var x = 5.4; //This will be of type double
```
5. Difference between the type dynamic and the keyword var:
```
void main() {
  dynamic a = 5;
  print(a.runtimeType); // int
  a = 7.0;
  print(a.runtimeType); // double
  a = 'test';
  print(a.runtimeType); // String
}

void main() {
  var a = 5;
  print(a.runtimeType); //int
  a = 7.0; // Error: A value of type 'double' can't be assigned to a variable of type 'int'
  a = 'test'; // Error: A value of type 'String' can't be assigned to a variable of type 'int'
}
```
6. Using the following: var a; without assigning a value to the variable, Dart will internally add the type dynamic to a. 
7. Sound Null Safety: Sound => Dart makes Static and Runtime Checks. Null Safety: Variables can't be null unless we explicitly say they can. 


**Thoughts**:  Most of the content today was a repetition of concepts, but I think I now really understand what Sound Null Safety means. And it seems that the type dynamic is a bit similar to the type mixed in PHP. 

**Links**: 
(Introduction to Dart - From Novice to Expert Tutorial Series)[https://www.youtube.com/watch?v=uZvoTCSsfjo&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7]
(#1 - Dart Language, Type System, Soundness, Type Inference, Null Safety, JIT & AOT Compilers)[https://www.youtube.com/watch?v=nQRW0_Q9RFI&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=2]


### Day 7: December 8, 2021

**Today's Progress**: Today, I started watching "The Best & Most Complete Dart Course - Visualize, Learn and Practice all Dart Language Concepts!" from Flutterly on youtube

**Learned**: 
1. For Mobile and Desktop, Dart uses two different compilers. Just In Time Compiler for development and an Ahead Of Time Compiler for compiling source code into machine code. Dart uses Dart Development Compiler and Dart to Javascript Compiler for the web.
2. Just in Time (JIT) Compiler only compiles the codes it needs to, and when that code is required, this is super smart during development. Because of JIT we can use hot-reload during development in Dart and Flutter.
3. Ahead Of time (AOT) Compiler compiles the entire source code into native machine code supported by the specific platform, and it does this ahead of time before the platform runs the program. 

**Thoughts**: Today's Dart session was a bit short. After finishing the course I watched the last few days, I felt a bit lost and unsure what to do next. I don't think I'm ready to move over to flutter already, so I spend some time looking for good content for learning Dart. And this 8h video might do it for me. 

**Links**: 
[The Best & Most Complete Dart Course - Visualize, Learn and Practice all Dart Language Concepts! Chapter 1.6 Dart Compilers at 13:55 min.](https://www.youtube.com/watch?v=F3JuuYuOUK4&t=937s)

### Day 6: December 7, 2021

**Today's Progress**: Today, I kept watching "Dart Programming in 4 hours | Full beginners tutorial" on youtube from Mike Dane. 

**Learned**: 
1. Object-Oriented-Programming (OOP). OOP makes it possible to create custom and complex data types, like a book or person. 
2. Class: A blueprint for the news data type. We should use CamelCase for class names. 
class Book {}
3. A class can have different attributes and methods.
``` 
class Book {
  String title;
  String author;
  int numPages;
}
```
4. Creating instances of a class => create an actual object of a class/datatype.
```
Book newBook = Book();
```
5. Contructor: 
```
class Book {
  Book(String name) { // Contructor that is used to initialize a new book
   	print("This ist the contructor of ${name}"); 
  }
}
```
Book newBook = Book("The new book"); // newBook is an object of the blueprint Book. 
6. Initialize a class attribute:
```
class Book {
 late String name;
  Book(String name) { 
   	this.name = name;
  }
}
```
7. The keyword "this" refers to the current object. 
8. Methods: The same as a function but placed inside a class.
```
class Student {
  late String name;
  late double gpa;

  Student(String name, double gpa) {
    this.name = name;
    this.gpa = gpa;
  }

  bool hasHonors() {
    return this.gpa >= 3.5;
  }
}
```
**Thoughts**: Okay, so the keyword new seems to be nonpresent in Dart - I might stumble over that when starting to write actual code. The constructor is just the name of the class, also pretty handy. 

**Links**:
[Dart Programming in 4 hours | Full beginners tutorial](https://www.youtube.com/watch?v=5xlVP04905w)


### Day 5: December 6, 2021

**Today's Progress**: Today, I kept on watching "Dart Programming in 4 hours | Full beginners tutorial" on youtube from Mike Dane. 

**Learned**: 
1. Switch statements:
```
switch(operator) {
	case '+':
		print("+");
		break;
	case '-':
		print("-");
		break;
	default: 
		print('Invalid operator');
}
```
2. While Loop: This is a programming structure that keeps running as long as the condition is true. 
```
int i = 0;
while (i < 5) { // loop guard
  print(i);
  i++;
 }
```
3. For loop:
for(int i = 0; i < 3; i++){
	print(i);
}
4. For loop (for iteratables)):
```
for(int i in [2,4,4]) {
  print(i);
}
```
5.Comments: 
```
// Singleline comment
/*
Multiline comment
*/
```

**Thoughts**: Today's session was a bit short. But some core concepts got introduced. I also managed to update some information on the Wiki for writers who would like to write an Interactive story to be published on the @storyways.app platform. But now work is calling!

**Links**:
[Dart Programming in 4 hours | Full beginners tutorial](https://www.youtube.com/watch?v=5xlVP04905w)


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

**Links**:
[Dart Programming in 4 hours | Full beginners tutorial](https://www.youtube.com/watch?v=5xlVP04905w)


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
