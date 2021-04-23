# 100 Days Of Code - Log

### Day 1: April 19, 2021 

**Today's Progress**: Setup the initial project. Create a client library for the weather. Attempt to connect to server as it runs.

**Thoughts:** I need to spin up a server when the integration tests start to run. Try this: https://www.danylkoweb.com/Blog/integration-testing-your-web-apis-FQ

**Link to work:** https://github.com/weekendprojectapp/100-days-of-code/tree/day-1-session-1

**Streams Links:**
* https://www.twitch.tv/videos/993582642
* https://www.twitch.tv/videos/993582642

**Stream Title:** 100DaysOfCode | Day 1 | Session 1/2 | Coding | Chatting

**Stream Category:** Science & Technology

**Stream Tags:** English, Programming, Web Development, Software Development, Educational, Tutorial


### Day 2: April 20, 2021 
**Today's Goals**: 
* E2E testing using MSTest and launching in a single session (both the client and server)

**Today's Progress**: 
* Create batch file to launch server during E2E testing
* Got deserialization of JSON working properly via case insensitivity
* Got E2E tests working
* Got POST method for /Weight started
* Got SQLite in-memory DB working (returns version)

**Thoughts:** 
* What does the LAUNCHER_PATH environment variable do?

**Link to work:** https://github.com/weekendprojectapp/100-days-of-code/tree/day-2-session-1

**Streams Links:**
* https://www.twitch.tv/videos/994525878
* https://www.twitch.tv/videos/994916511

**Stream Title:** 100DaysOfCode | Day 2 | Session 1/2 | Coding | Chatting

**Stream Category:** Science & Technology

**Stream Tags:**  Programming, Web Development, Software Development

### Day 3: April 21, 2021 
**Today's Goals**: 
* Spin up a SQL database from an embedded resource

**Today's Progress**: 
* Setup a Domain project
* Embedded a SQL schema file as a resource
* Created unit tests for the domain project
* Established a Gherkin like syntax for annotating our unit tests
* Able to parse embedded SQL files to generate a database 
* Installed https://sqlitebrowser.org/ to browse file based databases
* Implement POST on /Weight
* Store data in a database

** To Research:** 
* What does the LAUNCHER_PATH environment variable do?

**Streams Links:**
* https://www.twitch.tv/videos/995513555

**Stream Category:** Science & Technology

**Stream Tags:**  Programming, Web Development, Software Development, Tutorial, Educational

### Day 4: April 22, 2021 
**Today's Goals**: 
* Implement GET /Weight and GET /Weight/{id} endpoint
* Implement DELETE /Weight/{id}

**Today's Progress**: 
Session 1:
* Implement GET /Weight
* Discuss the role of architects in an organization
* Update Weight Table Schema. READ weight business logic and data built.
* GET list /Weight now works through the API
* GET by ID for weight now works.
* Rework E2E tests to leverage interfaces for the client
* Create a consistent pattern for dealing with lists / arrays returned with PageSize and NextPageToken
* Client SDK can now perform POST and GET (list) for weight using both Sync and Async methods
Session 2:
* Implement DELETE /Weight/{id} endpoint
* Implement GET /Weight/{id} endpoint
* Refactored the SDK to limit visibility into the guts of the client calls
* Created seperation between client SDK models and Request/Response REST DTOs

** To Research:** 
* What does the LAUNCHER_PATH environment variable do?

**Streams Links:**
* https://www.twitch.tv/videos/996902756
* https://www.twitch.tv/videos/997523265

**Stream Title:** 
* 100DaysOfCode | Day 4 | Session 1 | Coding | C#
* 100DaysOfCode | Day 4 | Session 2 | Coding | C#

**Stream Category:** Science & Technology

**Stream Tags:**  Programming, Web Development, Software Development, Tutorial, Educational

**Twitter:** 
* Live Stream: Day 4, Session 1 of #100DaysOfCode in #csharp, doing #API development. https://www.twitch.tv/highfiveboom
* Let's write some code! Live stream starting now: Day 4, Session 2 of #100DaysOfCode in #csharp, doing #API development. https://www.twitch.tv/highfiveboom