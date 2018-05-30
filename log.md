# 100 Days Of Code - Log

### Day 1: May 28th, 2018

**Today's Progress:** Started a book exchange / marketplace app. Setup the main framework with Node and HAPI. Setup Routing, and also added Swagger to document the API.  The basic API now returns the data in JSON format from the CSV input.

**Thoughts:**
The data file cleanup took a bit of time. Had to also wrap the _fs.ReadFile_ in a _Promise_. Need to set up a database and also make the code available online. That's for another day. Will link to Tweet for now.

**Link to work:** [Tweet for R1D1](http://bit.ly/2xm5qiG)

### Day 2: May 29th, 2018

**Today's Progress:** Fixed errors in Swagger that made testing the API calls fail and show no response. Was due to a CORS issue. Also tested several APIs for getting info from ISBN numbers. Created a repo for the project and mirrored it so that it is now on Github and Gitlab.

**Thoughts:** Small little things can cause so much aggravation and pain. Case in point, the CORS issue. Was caused by the server being configured with **_0.0.0.0_** as the host, and the browser checking **_localhost_** :) APIs also seem to change. Product API now needs confirmation and approval of Amazon Associate, which you only get with 3 purchases in 180 days which then triggers a review process.

**Link to work:** [ [Github](http://bit.ly/2snBVYg) | [Gitlab](http://bit.ly/2H4F3NQ) ]