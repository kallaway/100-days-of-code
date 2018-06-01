# #100DaysOfCode Log - Round 1 - Rohit Kilpadi

The log of my #100DaysOfCode challenge. Started on May 28th, 2018.

## Log

---
### R1D1 
Started a book exchange / marketplace app. Setup the main framework with Node and HAPI. Setup Routing, and also added Swagger to document the API.  The basic API now returns the data in JSON format from the CSV input.

The data file cleanup took a bit of time. Had to also wrap the _fs.ReadFile_ in a _Promise_. Need to set up a database and also make the code available online. That's for another day. Will link to Tweet for now.

[Tweet for R1D1](http://bit.ly/2xm5qiG)

---
### R1D2
Fixed errors in Swagger that made testing the API calls fail and show no response. Was due to a CORS issue. Also tested several APIs for getting info from ISBN numbers. Created a repo for the project and mirrored it so that it is now on Github and Gitlab.

Small little things can cause so much aggravation and pain. Case in point, the CORS issue. Was caused by the server being configured with **_0.0.0.0_** as the host, and the browser checking **_localhost_** :) APIs also seem to change. Product API now needs confirmation and approval of Amazon Associate, which you only get with 3 purchases in 180 days which then triggers a review process.

[ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### R1D3
Separated back end from front end in same repo. Back end is in Node + Hapi, Front end is in Angular 6 and Material. Also added Mocha, and Chai for testing purposes

Have to wrap my head around testing with Mocha and Chai before moving full speed ahead on the project. Need to get up to speed with the intricacies of Typescript and ES6.

[ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### R1D4
Working on Angular and Material. Fixed several errors. Created a new component and set up the basic version of it.

Lots of work still to do. Need to format the JSON output from the API into a better version. Still need to better understand some of the Angular 6 intricacies. The Material and FlexLayout for Angular6 are just not as well documented as the one for AngularJs.

[ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

