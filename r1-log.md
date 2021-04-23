# #100DaysOfCode Log - Round 1 - Mike de la Fuente

The log of my #100DaysOfCode challenge. Started on [Monday, April 19, 2021].

## Log

### R1D1 
* Created the initial project.

### R1D2
* Create batch file to launch server during E2E testing
* Get a more durable solution to launching the server for E2E tests
* Get all (1) tests to pass in an E2E manner

### R1D3
* Setup a Domain project
* Embedded a SQL schema file as a resource
* Created unit tests for the domain project
* Established a Gherkin like syntax for annotating our unit tests
* Able to parse embedded SQL files to generate a database 
* Installed https://sqlitebrowser.org/ to browse file based databases
* Implement POST on /Weight
* Store data in a database

### R1D4
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