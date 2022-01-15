# 100 Days Of Code - Log

### Day 15: January 15, 2022

**Today's Progress**: Today, I started doing some exercises from [this](https://hackmd.io/@kuzmapetrovich/S1x90jWGP) page and managed to do three exercises (3, 4 and 5). 

**Learned**:
1. Learned how to set the path to the Dart SDK in IntelliJ editor: Under preferences > Language & Frameworks > Dart
2. I have Dart installed twice on my machine at the moment, once as standalone installed with Brew and once with the flutter SDK.
3. Found and used the [documentation](https://api.dart.dev/stable/1.10.1/index.html) for Dart.
4. Learned a few ways on how to find the common unique members of two lists. 

**Thoughts**: 
It was nice to do some coding today and not do any theory besides reading in the documentation from Dart to find the methods I need. 


### Day 14: January 14, 2022

**Today's Progress**: I watched the video "#11 - Dart Built-in Types - num, int, double, String, List, Set, Map & Runes" from `Dart - from Novice to Expert`.

**Learned**:

1. Cast a string into an int:

```
void main() {
  String s = '5';

  int i = int.parse(s);
  double d = double.parse(s);
  num n = num.parse(s);

  print(i);
  print(d);
  print(n);
}
```

2. Cast int to a string:

```
   int i = 5;
   String s = i.toString();
```

3. The division operator returns a double value

```
void main() {
  int a = 3;
  int b = 4;

  var c = a/b;

  print(c); // 0,75
}
```

4. Get the truncate value of a division
Truncate means returning the integer obtained by discarding any fractional part of a number.

```
void main() {
  int a = 3;
  int b = 4;

  var c = a ~/ b;

  print(c); // 0
}
```

5. String interpolation and escaping a character:

```
void main() {
  double tempature = 33.4;
  String celcius = 'celsius';
  String s = 'It\'s $tempature ${celcius.toUpperCase()}';

  print(s); // It's 33.4 CELSIUS
}
```

6. String concatenation

```
void main() {
  String a = 'Hello ';
  String b = 'World';

  print(a + b); // Hello World
}
```

6. Multiline String:

```
String s = 'Hello \n World';
print(s); //Hello
World

String s2 = '''Hello
World''';
print(s); //Hello
World
```

7. Raw String:

```
void main() {
  String s = r'Hello \n World';
  print(s); // Hello \n World
}
```

8. Unicode

```
void main() {
  String unicode = '\u{1F339}';

  print(unicode); // 🌹
}
```

9. Lists are an ordered group of objects and can contain multiple types.

```
void main() {
   List<int> i = [1, 2, 3];
   List<bool> boolieans = [true, false, true];
   List<String> s = ['Hello', 'World', '!'];
   List<A> a = [A(),A()];

   List<num> listOfIntegersAndDoubles = [2, 3.4, 4];
   List<Object> listOfIntDoubleStrinAndBooelan = [2, 3.4, 'hey', true];
   List<Object?> listOfIntDoubleStrinBooelanAndNull = [2, 3.4, 'hey', true, null];
}

class A {

}
```

To access the methods and properties of values in the list, we need to cast them to the right type.

```
void main() {
  List<Object?> complexList = [2, 3.4, 'hey', true, null];

  var intValue = complexList[0] as int;
  var doubleValue = complexList[0] as double;
  var stringValue = complexList[0] as String;
  var booleanValue = complexList[0] as bool;
  var nullValue = complexList[0] as Null;
}
```

10. Nullable lists and lists with nullable values

```
void main() {
  List<int> a = [1, 2, 3];
  List<int?> b = [1, 2, null];
  List<int>? c = [1, 2, 3];
  List<int?>? d = null;
}
```

11. Different ways to assign lists:

```
void main() {
  List<int> a = [];
  List<int> b = [1, 3, 4];
  List<int> c = List.filled(3, 3);
  List<int> d = List.empty(growable: true);
  List<int> e = List.generate(3, (index) => index);

  print(a); // []
  print(b); // [1, 3, 4]
  print(c); // [3, 3, 3]
  print(d); // []
  print(e); // [0, 1, 2]
}
```

List literals ([]) are per default growable - meaning you can add new values to the list, after initiating them.

12. Dot operater (.) and null aware dot operator (?.)
    It can be used on an object to access class fields and methods.
    The null aware dot operator only accesses a field or method if the instance is not null and otherwise returns null.

```
void main() {
  int? a = 3;
  print(a.isEven); // false
  int? b = null;
  print(b?.isEven); // null --> its like saying, if the object is not null, then run the method isEven.
}
```

13. Cascade operator (..) and null aware cascade operator (?..)
    The Cascade operator allows us to make a sequence of operations on the same object. In addition to function calls, we can also access fields on that same object.

```
void main() {
  List<int> a = [];
  a.add(1);
  a.add(0);
  print(a); // [1, 0]

  List<int> b = [];
  b..add(2)..add(3);
  print(b); // [2, 3]
}
```

If a call returns void, you can’t construct a cascade on it.

14. Spread operator (...) and null aware spread operator (...?)
    The spread operator allows us to insert multiple values into a collection.

```
void main() {
  var a = [1, 2, 3];
  var b = [1, 3, 4];
  var c = [...a, ...b];
  print(c); //[1, 2, 3, 1, 3, 4]

  var d = null;
  var e = [...a, ...?d];
  print(e);
}
```

15. Collection if

```
void main() {
  bool promoActive = true;
  var nav = [
    'Home',
    'Furniture',
    'Plants',
    if (promoActive) 'Outlet'
  ];

  print(nav);
}
```

16. Collection for

```
void main() {
 var listOfInts = [1, 2, 3];
 var listOfStrings = [
  '#0',
  for (var i in listOfInts) '#$i'
 ];
 print(listOfStrings[1] == '#1');
}
```

17. List literals are not constant by default:

```
void main() {
  var a = [1, 2, 3];
  var b = [1, 2, 3];

  print(a.hashCode); // 175652764
  print(b.hashCode); // 1012260537
}
```

But we can make them compile-time constants by using the const keyword in front of the List literal

```
void main() {
  var a = const [1, 2, 3];
  var b = const [1, 2, 3];

  print(a.hashCode); // 73544676
  print(b.hashCode); // 73544676
}
```

18. Set: Sets are a collection of unordered unique objects.

Ways to declare a set:

```
void main() {
  var set = <int>{};
  var set1 = Set();
  var set2 = {'Hey', 'World'};
  var set3 = {1, 2, 3};
  var set4 = <int>{};
}
```
Example to show what set only has unique objects:
```
void main() {
  var set = <int>{};

  set.add(1);
  set.add(3);
  set.add(3);
  set.add(2);

  print(set); //{1, 3, 2}
}
```

Sets don't have an access operator like lists (set[0]). 

18. Maps - an object that associates keys and values
Each key must be unique - qual to JSON.

```
void main() {
  var map1 = {};
  var map2 = {
    1: 1,
    2: 2, 
    3: 3,
  };
  var map3 = Map();
  Map<String, int> i = {"key": 3};
  
  // Add new entry to map
  map1.addEntries([const MapEntry(1, 2)]);
  print(map1);
  
  // use spread operator with maps
  var map4 = {...map2};
  print(map4);
  
}
```

19. Runes - a collection containing all decimal Unicode code points of a String
```
void main() {
  var runes = Runes('hello').map((e) => e.toRadixString(16).padLeft(4, '0'),).toList();
  print(runes); // [0068, 0065, 006c, 006c, 006f]
  
  String hello = '\u{0068}\u{0065}\u{006c}\u{006c}\u{006f}';
  print(hello); // hello
}
```

**Thoughts**: This was a very loong tutorial - but it's always good to get the basics right and have a second look at them. 



### Day 13: December 14, 2021

**Today's Progress**: I watched the video "#10 - Dart Variables and the differences between Late, Var, Dynamic, Final & Const
`Dart - from Novice to Expert`.

**Learned**:

1.  Files outside a lib folder are not shared with other packages.
2.  There are four types of variables in Dart. They get their names depending on where they are declared:
    Top-level: variable that isn't linked to any class or object, they are accessible from anywhere in a program
    Static: Bound to a class or object.
    `static int i = 23;`
    Instance (also called fields/properties): Bound to a class or object.
    `double j = 33.4`
    Local: Variables with a local scope, for instance, inside a function.
3.  Nonnullable variables must be initialized (to a nun-null value) before being accessed or used.
    String car; --> this won't work, as Dart assigns null to the variable, but the variable type is not nullable.
4.  Static variables: Can be accessed without instantiating the class it lives in.

```
class A {
	static int i = 4;
}
void main() {
	print(A.i); // Output 4
}
```

5. Instance variables can be left unasigned if they get assigned in the contructor.

```
class A {
  int test;
  A({required this.test});
}
void main() {
  print(A(test: 2).test); // Output 2
}
```

6. Keyword `dynamic`: variable can change variable type; the variable can be reassigned to another value of any type.
7. Keyword `var`: variable can't change type but can be reassigned to another value of the sam type.
8. Keyword `final`: variable can't change type, and variable can't be reassigned to another value.
9. Keyword `const`: variable can't change the type and can't be reassigned to another value.
10. The keyword `const` can be used for variables, constructors and objects.

**Thoughts**: I did not develop a good idea for a small program to write, so I just watched some more theory.

**Links**:
[#10 - Dart Variables and the differences between Late, Var, Dynamic, Final & Const](https://www.youtube.com/watch?v=Efaq4LvS-es&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=11)

### Day 12: December 13, 2021

**Today's Progress**: I watched the video "#9 - Understanding Null Safety in Dart - Type Promotions, Null Assertion, Late, Required" from Flutterly's `Dart - from Novice to Expert`.

**Learned**:

1. null assertion operator (!): this is used to ensure that a nullable type isn’t null. This tells Dart that your expression is safe. (Using the `!` operator will make the code unsafe if the expression actually is null at runtime).
2. modifier `late`: can be used if you know that a variable will be initialized later than instantiating the class. (This also makes your code more unsafe, if you do forget to assign a value).

**Thoughts**: Not many thoughts today - the videos from Flutterly are super good and in-depth - but I would like to do some coding soon, so maybe I should come up with a small program that I could code.

**Links**:
[#9 - Understanding Null Safety in Dart - Type Promotions, Null Assertion, Late, Required](https://www.youtube.com/watch?v=ZZ4VVlggIVk&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=10)

### Day 11: December 12, 2021

**Today's Progress**: I watched the video "#7 - All you need to know about Dart Packages and the Pub Package Manager" from Flutterly's `Dart - from Novice to Expert`.

**Learned**:

1. Immediate dependencies: Are packages that your project depends on directly.
2. Transitive dependencies: Are packages that your immediate dependency depends on.
3. Regular dependencies: Are used in the development and production phases.
4. Dev dependencies: Are only used in the development phase. These packages are ignored when building the app for production.
5. `pubspec.lock` stores the current package information that your program depends on --> check this file into git so others install the same dependencies.
6. Code that shoud be exposed in a package should be located in the lib folder.
7. How to write a package and import it into another package by referencing the path to the locale package.

```
dependencies:
  calculator:
    path: 'packages/calculator'
```

**Thoughts**: Today, I got super tired just after I started to learn. So I decided to watch the video and take a break. I then started watching the video again and implemented all the steps necessary for creating a new package and using that in my existing project.
I guess private packages are usefull if you know you have code you will use in different projects. I always wanted to do this for my nuxt.js projects but somehow never managed - so ff you know how to do it, I would love to hear from you :)

**Links**:
[#7 - All you need to know about Dart Packages and the Pub Package Manager](https://www.youtube.com/watch?v=DciQbO_97oM&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=8)

### Day 10: December 11, 2021

**Today's Progress**: Watched two videos from Flutterly's `Dart - form Novice to Expert`

**Learned**:

1. Run your dart code with arguments:
   `dart run name_of_file arg1 arg2 arg3`
2. pubspec.yaml - is a file that keeps track of all the dependencies a project or package has.
3. pubspec.lock - automatically created when running the command
   `dart pub get`. This command is responsible for getting the current package's dependencies.

**Thoughts**: The second video today was about the Dart VM - and I must say I did not understand a lot of that. But learning about pub was super. It seems to be equivalent to Composer used in the PHP world.  
Yesterday I also dug into some flutter code, an existing project, and I learned that you could assign `const` to a widget with a variable in the constructor. I guess it makes sense. It took some time until I realized what was wrong, and in the end, I should just have read the error message to the end the first time. So - reading every line in an error message can save you some time :)

**Links**:

1. [#4 - Dart Project Components - Packages, Libraries, Lint Rules & Tests](https://www.youtube.com/watch?v=XnP3--55Uqo&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=5)
2. [#5 - Running a Dart Application In-Depth! - Dart VM, Dart Isolates, JIT & AOT Compilation](https://www.youtube.com/watch?v=NoVYI94MJio&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=6)

### Day 9: December 10, 2021

**Today's Progress**: Not too much Dart today. Had to upgrade homebrew and install macOs Monterey, which took a while.

**Learned**:

1.  SDK (Software Development Kit). Collection of tools for development
2.  Run a dart program with `dart run` --> for this command to work, locate the file containing the main() function in the bin/project-name.dart file.
3.  Dart Packages are associated with the following files and folders: .dart_tool, .pacages, pubspeck.lock, pubspeck.yaml.
4.  Libraries go into the lib folder.
5.  analysis_option.yaml - helps the Dart Static Analyser by following a set of rules called linting.
6.  Test folder is for tests.
7.  The bin folder is for command line apps.
8.  Dart Packages:

- pub.dev => collection of dart pacages.
- Application Package => a package what is not uploaded to pub.dev
- Library package => a package what is uploaded to pub.dev

**Thoughts**:

**Links**:

1. [#2 - How to install the Dart SDK on Windows, Linux and MacOS](https://www.youtube.com/watch?v=WIO5iAeNaOU&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=3)
2. [#4 - Dart Project Components - Packages, Libraries, Lint Rules & Tests](https://www.youtube.com/watch?v=XnP3--55Uqo&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=5)

### Day 8: December 9, 2021

**Today's Progress**: I started the youtube track "Dart - from Novice to Expert" from Flutterly. I watched the first two videos.

**Learned**:

1.  Static type check => happens while writing code when Dart tries to compile your code. If your code isn't type-safe, your editor will show an error. And should prevent the Developer from writing the wrong types.
2.  Run time check => an extra assessment that happens when the program is running.
3.  Sound type system: Dart won't allow the code to run into an undefined state.
4.  Dynamic types. Dart won't perform type checks on dynamic types. You will have to do this yourself to avoid an exception at runtime. But at runtime Dart will infer what type the data is.

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

**Thoughts**: Most of the content today was a repetition of concepts, but I think I now really understand what Sound Null Safety means. And it seems that the type dynamic is a bit similar to the type mixed in PHP.

**Links**:

1. [Introduction to Dart - From Novice to Expert Tutorial Series](https://www.youtube.com/watch?v=uZvoTCSsfjo&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7)
2. [#1 - Dart Language, Type System, Soundness, Type Inference, Null Safety, JIT & AOT Compilers](https://www.youtube.com/watch?v=nQRW0_Q9RFI&list=PLptHs0ZDJKt_fLp8ImPQVc1obUJKDSQL7&index=2)

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

Book newBook = Book("The new book"); // newBook is an object of the blueprint Book. 6. Initialize a class attribute:

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
