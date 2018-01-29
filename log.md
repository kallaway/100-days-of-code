# 100 Days Of Code - Log

### Day 1: Jan 18, 2018

**Today's Progress**:

- Started setting up the lambda server for brain of my bot.
- Created an endpoint to return true or false if progress log.md (this file) was updated with today's progress.

**Thoughts:** Setup Python3 env, Zappa and basic Flask App. Feels like it took 1.5 hrs to just setup and play with simple github API, need to improve my speed. Refactored logic and simplified requirements in second pass

**Link to work:**

- [API endpoint:=> /brain/api/v1.0/logs/is_updated_today](https://6kvjel14vk.execute-api.us-east-1.amazonaws.com/dev/brain/api/v1.0/logs/is_updated_today)


### Day 2: Jan 19, 2018

**Today's Progress**:

- Created webhook for messenger bot to talk to
- Connected messenger bot to api, simple bot set-up

**Thoughts:** Need to spend more time reading fb messenger api. Should not be that hard. Github example repo was super helpful to quickly get things up and running. Will need to refactor brain.py soon.

**Link to work:**

![Stackbot](images/screenshot_19_01_18.png)


### Day 3: Jan 20, 2018

**Today's Progress**:

- Refactored code, more to go
- Fixed Timezone bug
- Added notification for no progress update

**Thoughts:** Need to start writing tests. Weekends should be heavier than couple 100 lines of push. Push Push Push!!

**Link to work:** Nothing to show yet


### Day 4: Jan 21, 2018

**Today's Progress**:

- Refactored logging code, more to go
- Bot notifies me if the weather is very cold (feels like < -10) or plesant in winter (feels like > 0)
- New Name, New Logo

**Thoughts:** Need to start writing tests. Push Push Push to write heavier pieces!!

**Link to work:** ![JainBot](images/screenshot_21_01_18.png)

### Day 5: Jan 22, 2018

- Solved Programming assignment for [Classification Course](https://www.coursera.org/learn/ml-classification)
- Warming up to sklearn functions and skills

**Thoughts:** Making and evaluating simple baseline models is quite easy. I should practice it more often. That way I will not have to relearn the scipy api over and over again.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_1.ipynb)

### Day 6: Jan 23, 2018

- Completed Assignment 1 and Quiz
- Started on Hypothesis Testing

**Thoughts:** Working throught it

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_1.ipynb)


### Day 7: Jan 24, 2018

- Completed creating Feature Matrix for Assignment 1 Week 2
- Added security for APIGateway Endpoint

**Thoughts:** I love the habit of accomplishing something everyday :)

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_2.ipynb)


### Day 8: Jan 25, 2018

- Assignment 1 Week 2 complete. Implemented logistic regression and gradient ascent by hand.

**Thoughts:** Working through it is fun. Try and work on assingments with blank slate instead of pre-filled template in coursera as it makes things easier/spood fed. :)

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_2.ipynb)


### Day 10: Jan 27, 2018

- Devops code completed to spin a EC2 instance to provision it to run jupyterhub where I can host my ipython notebooks.

**Thoughts:** This is a piece of Infra as code I want to build, for data teams in fast growing companies. There are still some tweaks left and clean up is required to ship it properly.

**Link to work:**  /code/datascience-infra of this repository


### Day 11: Jan 28, 2018

- Completed Quiz 2 and Derived derivative of log likelihood for gradient ascent.
- Worked through lectures till overfitting, L@ regularisation left

**Thoughts:** Sunday was a good day for consuming lectures and spending time understand the concepts. Happy with my progress on it. Assignment and L2 next.

**Link to work:** ![Quiz](images/quiz2.png) ![Derivation Result](images/loglikelihood_proof.jpeg)

