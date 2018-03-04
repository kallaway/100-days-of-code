# Microsevices

Some questions to answer:

- How big/small should a microservice be?
- How should the microservices interact? API/Messaging Queue/DB
- How should I partition my monolith into microservices?
  - How should I partition my data in the monolith
  - How should I deal with logging, config and env variable management etc as discussed in the [Twelve Factor App](https://12factor.net/)

Started with [Principles of MICROSERVICES](https://www.safaribooksonline.com/library/view/the-principles-of/9781491935811/)

What are the **advantages** of microservices?

- Better alignmnet within organisation.
- Speed to market for features can increase drastically. Deployment and testing only concerns the current change in a small autonomous service instead of the big app which requires a big deploy for small delta.
- Small and many components so its not a single point of failure.
- Security can be custom made for services. Payment service team can work on security while while catalogue delivery team can focus on other things.
- Data can be partitioned so when the business grows, small components grow individually.


What are the **disadvantages**?

- The process is front loaded so takes time to show the impact.
- Testing microservices can become painful. Especially when testing end to end features and flows with multiple components.
- Finding cause of errors and problems through monitoring can be hard. There are many components which can have a casading effect
- Resiliency is hard too



### Major Principles of microservices:

1. Services should be modeled around business domains
2. Culture of automation should be embraced throughtout the org
3. Decentralise all things
4. Consumers first
5. Isolate failures


### 1. Modeled around business domains

- slice your monolith vertically not horizontally
- ui/logic/data is horizontal, instead it should be payments/customers/catalogue
- services that change together should stay together


### 2. Culture of automation

- API driven declarative provisioning
- Custom container/image for speed
- Continuous delivery
- Automated testing

#### 3. Hide implementation details

- Hide your databases
- Most common flaw is sharing same db-model code but if you think about it, different context bound services should store different data for same entity. For example: sales/support will both want to store customer but in different ways
- Think about communication protocols.

### 4. Autonomy = Decentralisation

- Each team should be able to build it, run it, operate it, decommision it. Team will become expert in business domain of their service
- Promote internal open source where teams can contribute to other services like open source environment
- Orchestrator vs Chereographer
- Use event based communication. So choreographer is loosely coupled with actors and this model can scale very well.


### 5. Deploy Independently

- Small independent changes should be easily deployable. This can be done only when # 3 is done correctly.
- Its ideal to have one service per os as there can be side effect like (resource utilization if that is not the case)
- When breaking changes are made, consumer driven contracts can be enforced with tests provided by the consumer. It is a trust base model to deploy to production if consumer tests pass.
- [Packt.io](https://docs.pact.io/) for consumer driven contract testing
- Co-existence of different service versions can be tricky. Some solutions:
  - different services for different versions. Service discovery becomes complex in this scenario. 2 main downsides
    - now code needs to be release and changed in the different branches that we serving customers
    - if it is a stateful service, the data consistency required between the services is another new challenge that needs to be solved
  - solution 2 is different endpoints. service.com/v1/ service.com/v2
    - this relies on the ability for the consumers to be able to change their code quickly.


### 6. Consumer First

- Documentation can help consumers understand how to use your api effectively
- swagger is a good tool for that
- [paypal api guide](https://github.com/paypal/api-standards/blob/master/api-style-guide.md)
- Monitor consumer access patterns to make sure the services is being used correctly and SLAs are met.
- Note to self: Opensource API-Gateway tooling is lacking and an ooportunity to innovate in. https://tyk.io/#section-3 looks like something interesting.


