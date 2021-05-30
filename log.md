# 100 Days Of Code - Log
#100DaysOfCode 2nd_rap Day: 001/100  
I am going to try for 2nd rap from today!  
I learned Linux command "nslookup".  
It is used to check the status of DNS server settings. And to check DNS-related setting in DNS clients.  
To use "nslookup command" , I need to install a package called "dnsutils"  

```bash
$ sudo apttitude install dnsutils
```
```bash
$ nslookup tatatamaki.com
Server:		133.***.*.***
Address:	133.***.0.3#53

Non-authoritative answer:
Name:	tatatamaki.com
Address: 133.***.**.***
```
#100DaysOfCode 2nd_rap Day: 002/100
I have created an MyMyCertificate.
I make three files.
- Private key server.key
- CSR server.csr
- CRT server.crt

$ openssl genrsa 2048 > server.key
$ openssl req -new -key server.key > server.csr
$ openssl x509 -days 3650 -req -signkey server.key < server.csr > server.crt

Then, I write the necessary information in the configuration file.
Normally, this would work, but it didn't.
Why?? MyMyCertificate !!

Life and programming don't always work out according to the manual...Aww
I will try again tomorrow !!

#100DaysOfCode 2nd_rap Day: 003/100
I try At Coder from today.
I learned the "gets method", the "split method".
The "gets method" is a method to get the value entered by the keyboard from the terminal as a string.
The "split method" splits the string with the specified delimiter and returns it as an array.
Code to determine whether a number is even or odd.
It is passed as a, b in the standard input(STDIN).

a, b = gets.split(' ')
ax = a.to_i
by = b.to_i
c = ax * by

if c.even?
	puts "Even"
else
	puts "Odd"
end

#100DaysOfCode 2nd_rap Day: 004/100
I try AtCoder.
https://atcoder.jp/contests/abs/tasks/abc081_a
It was supposed to be the easiest problem, but it was too hard.
But I cleard it.
The key is to write a one-line map(block)sentence.

arry = gets.chars
total = arry.map { |n| n.to_i }

p total.count(1)

#100DaysOfCode 2nd_rap Day: 005/100
I read about recursive functions today.
https://qiita.com/drken/items/23a4f604fa3f505dd5ad#fn1
This is a broad concept. As long as it calls itself, it is recursive.

def sum(arry)
	return 0 if arr.empty?
	top = arry.shift
	top + sum(arry)
end
p sum([1,2,3,4,5]) #=> 15

#100DaysOfCode 2nd_rap Day: 006/100

I learned Proc Object.
I want to use block as objects.
So, Proc is an object of the Block.
Add a parameter with & to the end of the temporary argument of a method definition.
hoge → Proc Object, &hoge → block

def foo_method(&hoge)
p hoge.call
end

foo_method { "test" }
=> "test"

#100DaysOfCode 2nd_rap Day: 007/100
I review for_syntax.
The process is repeated.
And, extract the elements from the array one by one and display them respectively. 

names = ['jhon', 'paul', 'george', 'ringo']
for name in names
puts name
end

#100DaysOfCode 2nd_rap Day: 008/100
I tried AtCoder. (ABC081B - Shift only)
I use "while sentence".
When the condition (if % 2 == 0) is met, assign the number divided by 2 to the variable i, and perform loop processing.
And, when the boolean is true, count is increased by 1.
When the boolean is false, it is out of the block.
Count will be assigned to the result variable as the return value.
Finally, in "result.min", output the smallest number among the return values.

n = gets.chomp.to_i
arry = gets.chomp.split(" ").map(&:to_i)

result = arry.map do |i|
	count = 0
	while i % 2 == 0 do
		i = i /2
		count += 1
	end
	count
end
puts result.min

#100DaysOfCode 2nd_rap Day: 009/100
Let's review "Hash" today !
What is "Hash" ?
An object of the Hash class that manages multiple data with a set of key/value combinations.
Can change the value by specifying a key.
Usse symbols, not strings, for hash keys!
But, I love Keith Richards better than Hash key !!

TheRollingStones = { Mick: "vacal", keith: "guitar", Ron: "guitar", Charlie: "Drums" }
	TheRollingStones.each do | name, part |
	puts "#{name} plays #{part}"
end

#100DaysOfCode 2nd_rap Day: 010/100
Self-assignment operator using || in Ruby.
a ||= 10 will return 10 if the variable a does not exist (nil or false).
a = nil or false
a ||= 10
=> 10

But、if the variable contains a value, assign it to a and use it as the return value.
a = 20
a ||= 10
=> 20

#100DaysOfCode 2nd_rap Day: 011/100
I create sql table.
The basics of the SELECT statement.

CREATE TABLE table_name
(
column_name data_type constraints,
shohin_mei CHAR(4) NOT NULL
);

The columns of the got table can be output.
SELECT get_column_name, get_column_name,,,,
FROM table_name;

And, if you specify a condition, it will retrieve the data that meets the condition.
SELECT shohin_mei, shohin_bunrui
FROM shohin
WHERE shohin b_bunrui = 'foo';

#100DaysOfCode 2nd_rap Day: 012/100
I tried AtCoder. (A - Century)
This question's point is Algorithm and .floor method.

n = gets.chomp.to_i
x = (n + 99) / 100
puts x.floor

When I was solving this problem, I thought again today. 
I'm not very good at thinking of algorithms.
It's fatal, but I have to do a lot of work and get used to the patterns.

I remember famous Japanese comedians saying, "Other people's children and bitter melons grow up fast."
Others are strangers. Don't worry about it!
Is it possible for adults to improve their academic skills in a subject they are not good at? It's an experiment with my own body!
I will do my best!!

#100DaysOfCode 2nd_rap Day: 013/100
I tried AtCoder. (A - Square Inequality )
No particular point.
It's a redundant code, but I did it without looking anything up just to make it work.

arry = gets.split(" ").map { |n| (n.to_i) **2 }

if arry[0] + arry[1] < arry[2]
puts "Yes"
else
puts "No"
end

#100DaysOfCode 2nd_rap Day: 014/100
I tried AtCoder. (A. Div)
Today's problem was not specifically related to ruby.
Just read the question text and answer.
Literacy is important.

n = gets.chomp.to_i
puts n-1

#100DaysOfCode 2nd_rap Day: 015/100
I tried AtCoder.(A. Rotate)

This sentence will cause an error.
arry = gets.split('')
s = arry.rotate
puts s.join('')

It was cause O.k.2
s = gets
puts s[1]+s[2]+s[0]

W~h~y~ AtCoder~?? said.(In the style of Atsugiri_Jason.)
I don't have a choice. I'll settle for this.

#100DaysOfCode 2nd_rap Day: 016/100
I tried AtCoder.(A - Difference Max)

I wrote first code. But, this code is error.
ab = gets.split(' ')
front_part = ab.max.to_i
cd = gets.split(' ')
back_part = cd.min.to_i
puts front_part - back_part

It is next code. But, this code is error. 
ab = gets.split(' ').max.to_i
cd = gets.split(' ').min.to_i
puts ab - cd

Third time's a charm !!
Success!!!
a, b = gets.split.map(&:to_i)
c, d = gets.split.map(&:to_i)
puts [a, b].max - [c, d].min

#100DaysOfCode 2nd_rap Day: 017/100
I tried AtCoder.(A - Health M Death)
This time, I was able to attack it simply with an "if statement".
The point is to perform a surplus calculation(operator => %).

m, h = gets.split.map(&:to_i)
if h % m == 0
puts "Yes"
else
puts "No"
end

#100DaysOfCode 2nd_rap Day: 018/100
I tried AtCoder.(A - I Scream)
This is an ice cream problem.
I'm going to have ice cream today.
A taste of home after a long absence, Blue Seal !!

a, b = gets.split.map(&:to_i)
	if a + b >= 15 && b >= 8
		puts 1 
	elsif a + b >= 10 && b >= 3
		puts 2
	elsif a + b >= 3
		puts 3
	else
		puts 4
	end

#100DaysOfCode 2nd_rap Day: 019/100
I tried AtCoder.(A - Discount)
Use method String#to_f to get the decimal point.
You get what you pay for.

a, b = gets.split.map(&:to_f)
discount = (1 - b / a) * 100
p discount

#100DaysOfCode 2nd_rap Day: 020/100
I tried AtCoder.(A - Star)
I remembered the Fizzbuzz Quiz.
Good old days~!

x = gets.chomp.to_i
(1..100).each do |n|
	if (x + n)  % 100 == 0
		puts n
	else
		next
	end
end

#100DaysOfCode 2nd_rap Day: 021/100
I tried AtCoder.(A - Vanishing Pitch)
Use the conditional operator　"||".
Lately, I've been enjoying watching Major League Baseball player Otani's activities !!
Big fly !! OooootaniSaaaan !!

v, t, s, d = gets.split.map(&:to_i)
invisible_ball_start = v * t
invisible_ball_finish = v * s
if invisible_ball_start > d || invisible_ball_finish < d
puts "Yes"
else
puts "No"
end

#100DaysOfCode 2nd_rap Day: 022/100
I tried AtCoder.(A - Very Very Primitive Game)
It took me a long time.
In the end, the output was just the opposite.
Fall and fall, but I get up and keep going. Like a Rolling stone !!

a, b, c = gets.split.map(&:to_i)
if c == 0 && a <= b
puts "Aoki"
elsif c == 1 && a < b
puts "Aoki"  
else
puts "Takahashi"
end

a, b, c = gets.split.map(&:to_i)
if c == 0
puts a <= b ? "Aoki" : "Takahashi"
elsif c == 1
puts a < b ? "Aoki" : "Takahashi"
end

a, b, c = gets.split.map(&:to_i)
if c == 0 && a <= b
puts "Aoki"
elsif c == 0 && a > b
puts "Takahashi"
elsif c == 1 && a < b
puts "Aoki"
elsif c == 1 && a >= b
puts "Takahashi"
else
puts  "Aoki"
end

#100DaysOfCode 2nd_rap Day: 023/100
I tried AtCoder.(A - Slot)
I would like to use a method and go for it, but I'm not sure what I'm capable of right now.
Keep trying!!

c = gets.to_s.chars
if c[0] == c[1] && c[1] == c[2]
puts "Won"
else
puts "Lost"
end

#100DaysOfCode 2nd_rap Day: 024/100
I tried AtCoder.(A - Three-Point Shot)
Received as an array, sorted, and calculated.
It's so redundant!
Redundant, which sounds like Linda Linda.
A punk band apparently named after a Japanese punk band(THE BLUE HEARTS).
COOL !!
https://twitter.com/LAPublicLibrary/status/1395485852579495936?s=20

arry = gets.to_s.split.map{ |e| e.to_i }
s = arry.sort
score = s[1] - s[0]
result = score < 3 ? "Yes" : "No"
puts result

#100DaysOfCode 2nd_rap Day: 025/100
I forgot to tweet this yesterday.
Guard Clause is one of the techniques to avoid deep nesting of conditional branches, 
and is sometimes translated as "guard clause", "guard condition", or "guard syntax".
It is sometimes referred to as "early return" because of its behavior.

def ranking(point)
return 'gold' if point > 90
return 'silver' if point > 70
return 'bronze' if point > 50
'PrizeForParticipation'
end

#100DaysOfCode 2nd_rap Day: 026/100
I tried AtCoder.(A - Brick)
I'm getting used to that A problem.
Let's work on problem B next time.

n, w = gets.split.map(&:to_i)
brick = n / w
puts brick

#100DaysOfCode 2nd_rap Day: 027/100
I tried AtCoder.(B - 180°)
First try B problem.
It was difficult, but I managed to get through it.
Keep going !!

s = http://gets.to_s.split("")
x = s.reverse.join
y = http://x.tr('69', '96')
puts y

#100DaysOfCode 2nd_rap Day: 028/100
I tried AtCoder.(A - ABC Preparation)
Today first, I tried problem B, but it was too difficult to solve.
I had to start from problem A again.

a = gets.to_s.split.map{ |e| e.to_i }
puts a.min 