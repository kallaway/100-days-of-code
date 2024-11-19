# 100 Days Of Code - Log

### Day 1: May 28th, 2018
**Today's Progress:** Started a book exchange / marketplace app. Setup the main framework with Node and HAPI. Setup Routing, and also added Swagger to document the API.  The basic API now returns the data in JSON format from the CSV input.

**Thoughts:**
The data file cleanup took a bit of time. Had to also wrap the _fs.ReadFile_ in a _Promise_. Need to set up a database and also make the code available online. That's for another day. Will link to Tweet for now.

**Link to work:** [Tweet for R1D1](http://bit.ly/2xm5qiG)

---
### Day 2: May 29th, 2018
**Today's Progress:** Fixed errors in Swagger that made testing the API calls fail and show no response. Was due to a CORS issue. Also tested several APIs for getting info from ISBN numbers. Created a repo for the project and mirrored it so that it is now on Github and Gitlab.

**Thoughts:** Small little things can cause so much aggravation and pain. Case in point, the CORS issue. Was caused by the server being configured with **_0.0.0.0_** as the host, and the browser checking **_localhost_** :) APIs also seem to change. Product API now needs confirmation and approval of Amazon Associate, which you only get with 3 purchases in 180 days which then triggers a review process.

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 3: May 30th, 2018
**Today's Progress:** Separated back end from front end in same repo. Back end is in Node + Hapi, Front end is in Angular 6 and Material. Also added Mocha, and Chai for testing purposes

**Thoughts:** Have to wrap my head around testing with Mocha and Chai before moving full speed ahead on the project. Need to get up to speed with the intricacies of Typescript and ES6.

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 4: May 31st, 2018
**Today's Progress:** Working on Angular and Material. Fixed several errors. Created a new component and set up the basic version of it.

**Thoughts:** Lots of work still to do. Need to format the JSON output from the API into a better version. Still need to better understand some of the Angular 6 intricacies. The Material and FlexLayout for Angular6 are just not as well documented as the one for AngularJs.

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 5: June 1st, 2018
**Today's Progress:** JSON output from API endpoint works now.
Booklist now shows book covers from the OpenLibrary API.

**Thoughts:** Need to get better data source for the API. Improve Layout. Need to study Material and Flex a bit more in depth for Angular 6. Still having trouble getting it to do what could be easily done in Angular 1x with Material

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 6: June 3rd, 2018
**Today's Progress:** **Lambda** functions, **serverless architecture** oh my! :) Planning on moving some of my projects to **AWS** to better utilize serverless architecture

**Thoughts:** Didn't code yesterday. Did tutorials & read up on new tech that I want to use, but no code so doesn't count. 

**Link to work:** [Tweet for R1D6](http://bit.ly/2JqnJbl)

---
### Day 7: June 4th, 2018
**Today's Progress:** API research and testing for book metadata retrieval and some coding around [SQLite](http://bit.ly/2sCFnhy) to prepare for the main core of the project

**Thoughts:** Need to work more on testing with [Mocha](http://bit.ly/2HlFwLK) and [Chai](http://bit.ly/2sBuZXw). Not being very consistent. It is a little tricky to set up and I get too impatient

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 8: June 6th, 2018
**Today's Progress:** Studied and tried out various service worker scripts and AWS Lambda. Focused on Angular 6.

**Thoughts:** Serverless architecture is really interesting!

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 9: June 7th, 2018
**Today's Progress:** Partially migrated a theme from Pixelarity to a Ghost Theme. This will be used as the main site for my projects and I will be moving some of the jquery scripts to Angular 6.

**Thoughts:** Difficult to find time every single day for coding that is not work related. Not giving up though .. just restarting with vigor.

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 10: June 9th, 2018
**Today's Progress:** Worked on website for the project. Should be ready and public in a couple of days

**Thoughts:** Wonder whether it is better to keep website, angular app, and api separate or to run them unified

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 11: June 10th, 2018
**Today's Progress:** Did some coding tests and working through some advanced Angular 6 concepts

**Thoughts:** Going to keep the three parts separate for now.

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]

---
### Day 12: June 11th, 2018
**Today's Progress:** Worked on the website design for the main site as well as some Material and Flex with Angular 6. Very basic angular part is [now online](http://bit.ly/2l5fBiG) This will be fleshed out and improved

**Thoughts:** Need to work on the UX/UI

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) | [Demo](http://bit.ly/2l5fBiG) ]

---
### Day 13: June 27th, 2018
**Today's Progress:** Set up API with a very rough import function into a local sqlite3 database. The import function is really very rough. Will refactor later

**Thoughts:**  Will investigate differences between local sqlite3 and Mongodb Atlas

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) | [Demo](http://bit.ly/2l5fBiG) ]
