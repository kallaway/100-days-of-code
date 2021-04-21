# Project Plan
## Things I've built before:
* Credit Card Processing Platform
* Document Management System
* Games

## What should I build:
* Metric API service

## Topics to touch on:
* How to run E2E tests from a client to a server when they exist in the same solution
* E2E vs Unit Tests
* Generating Mock Data
* Fluent Assertions
* TDD
* CORS
* Implementing a PATCH endpoint
* Field masks
* Update masks
* Filters for an API
* HttpClient pooling
* Client side error reporting - Exceptionless
* Gherkin / Cucumber
* Initializing data for testing
* Spinning up databases on the fly / per test run
* Performance Analysis / profiling code on your machine
* Logging
* Tracing
* Distributed Tracing
* Load Testing (all the time)
* API Proxies (Apigee vs Kong)
* OpenAPI Specs
* Setting up a CI/CD pipelines
* Database migrations
* Sketching an idea vs. creating something more production ready (v1 vs v2)
* Dockerizing a project (and why)
* Using a service bus / task queue
* gRPC vs REST
* Chunking data into an API
* Code Coverage
* Running tests as part of the build
* MATs vs E2Es vs Unit Tests
* Adding a Vue/React frontend to you services
* Backend for Frontends (BFF)
* ORM vs Hand-written SQL - performance
* Performance testing your SQL
* Connection pooling
* Caching on the client vs caching on the server
* Compound APIs
* OAuth2
* Developer Keys vs OAuth2
* Throttling
* Monitoring and Alerting
* Fluent API clients
* JWTs for everything


### Metric topics:
* Weight
* Exercise (Run)
* Nutritional Macros (Calories / Nutrients / Fat / Protein / Carbs)

### Weight:
Date Time - Measurement - Units - Person (Identifier)
Units:  Mass - Grams/Kilograms, Pounds, Ounces

**POST /Weight**
{
	DateTime: string (ISO),
	Value: 185.5,
	Unit: string ("pounds", "kilograms", "ounces", "stones")
}

### Height:
Date Time - Measurement - Units - Person (Identifier)
Units: Length - Meters, Feet

### API Calls:
Start Date Time - End Date Time - Measurement - Units - System - Endpoint
Units: Calls / Period

### Error Incidents:
Start Date Time - End Date Time - Measurement - Units - System - Error Type
Units: Incidents / Period