# Day 1 -

## Description

This recreates the first day project from [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) written in Go.

I am working through the class at work in Python, and on my own time am re-implmenting my solutions in Go as a way to strengthen ideas, but also learn another programming language.

## Setup & Run Instructions
```
$ go build bandname
$ ./bandname
Input the name of your city:
Night City
Input the name of your pet:
Maelstrom
Your band name should be the Night City Maelstrom
```

## Lessons Learned
I didn't initially realize that `fmt.Scan(&i)` would only grab one word and not everything typed into a string.

This lead me to find the `bufio.NewReader` module.  This brought it's own challenge, as using a `\n` newline as the delimiter would actually add the newline to the captured string.

I finally was lead to figure out how to strip that trailing newline from each of the variables.  I'm unsure if there is a cleaner way to solve this or not.
