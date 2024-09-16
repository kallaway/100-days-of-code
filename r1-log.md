# #100DaysOfCode Log - Round 1 - [Ismail ElFadli]

The log of my #100DaysOfCode challenge. Started on [December 10, Sunday, 2017].

## Log

### R1D1 
Joing the Python Course on https://www.codecademy.com/learn/learn-python I complete 19% of it, it was my first time working with the "datetime" library.
by watching a tutorial on https://www.youtube.com/watch?v=Z9fIBT2NBGY, now I can use Git to make version of my code and to publish it on a public server [I recommend everyone who want to start working with git and github to watch it]

### R1D2
I start coding at night with **R**.
Get started with *Bioconductor* package in *R*, *BSgenome* package to work with whole-genome sequence data, using **seqnames** function to find the names of each chromosome on the genome : ```seqnames(BSgenome.Hsapiens.UCSC.hg19)```. wanna know the length of the chromosome, just write: ```length(hg19[["chr22"]]).```
The **alphabetFrequency** function is a very useful and eficient tool provided by Biostrings for calculating the number of occurences of each DNA base within a given DNAString. ```alphabetFrequency(hg19[["chr22"]],baseOnly=TRUE)``` using baseOnly to tell the function to use only valid DNA bases.
Finding the occurs of seq:
```
s1 <- "aaaatgcagtaacccatgccc"
matchPattern("atg", s1)
```
### R1D3
Even I was tired, I traveled from Rabat to Marrakech, I didn't want to sleep until done my work.
I continue my progress on Python Course (codeacademy) **if, elif, else**, and then I move to Linux with **H3ABioNet** course ( I did the first assignment), how to move throgh linux environment (absolute path, relative path, pwd, ls, mkdir, rmdir).
https://training.h3abionet.org/IBT_2017/?page_id=915

### R1D4
Go on with linux commands, use ```touch``` to create file, ```nano``` to ediText, other commands to manipulate files ```cat,less,tail..```, Copy,	move	and	remove files ```cp mv rm```and ```wget```.
[wget advance](https://www.labnol.org/software/wget-command-examples/28750/).
I start the second assignement (question N5).

### R1D4
I didn't have the time last night to write what I did. I still with linux.
* how to extract information from files, ```wc``` for word count, ```sort, join, diff, uniq, grep```.
* Redirection	of	the	output	result	to	a	file	is	possible.	```command options	filename.in > filename.out```.
*  Combining	several	commands	is	done	thanks	to	the	use	of	a	“|”	character. ```command1 optioons1	filename1.in |command2 options2	> filename.out.```

### R1D4
I'm not happy, two days ago I didn't code a lot, just few minitues, but today [17-12-2017] I started **Regular Expression** using python
based on this book [Chapter 7 – Pattern Matching with Regular Expressions](http://automatetheboringstuff.com/chapter7/).
