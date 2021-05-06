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

























