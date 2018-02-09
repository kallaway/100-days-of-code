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

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_2_1.ipynb)


### Day 8: Jan 25, 2018

- Assignment 1 Week 2 complete. Implemented logistic regression and gradient ascent by hand.

**Thoughts:** Working through it is fun. Try and work on assingments with blank slate instead of pre-filled template in coursera as it makes things easier/spood fed. :)

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_2_1.ipynb)


### Day 10: Jan 27, 2018

- Devops code completed to spin a EC2 instance to provision it to run jupyterhub where I can host my ipython notebooks.

**Thoughts:** This is a piece of Infra as code I want to build, for data teams in fast growing companies. There are still some tweaks left and clean up is required to ship it properly.

**Link to work:**  /code/datascience-infra of this repository


### Day 11: Jan 28, 2018

- Completed Quiz 2 and Derived derivative of log likelihood for gradient ascent.
- Worked through lectures till overfitting, L@ regularisation left

**Thoughts:** Sunday was a good day for consuming lectures and spending time understand the concepts. Happy with my progress on it. Assignment and L2 next.

**Link to work:** ![Quiz](images/quiz2.png) ![Derivation Result](images/loglikelihood_proof.jpeg)



### Day 12: Jan 29, 2018

- Assignment 3 50% complete. Finished lecture content on L2 Regularisation for Logistic Regression.

**Thoughts:** Working through it. Late night math can be hard to digest and takes more time.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_2_2.ipynb)


### Day 13: Jan 30, 2018

- Assignment 3 completed and associated quiz submitted.
- Did some reading to write a new blog post on aws cost saving.

**Thoughts:** Working through it.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_2_2.ipynb)


### Day 14: Jan 31, 2018

- [Things I dont know Gist](https://gist.github.com/nehiljain/714ab790cb6774ecc71d39a24e222081)
- Seaborn heatmap to learn about quick correlation analysis on datasets
- Added [Post-Save Hook for jupyter workflow](https://towardsdatascience.com/version-control-for-jupyter-notebook-3e6cef13392d).

**Thoughts:** Jupyter notebook post-save hook is major key for version control and peer-reviewed workflow. Correlation is a basic tool and I want to learn to become good at finding variables that are correlated. It can directly help make business decision when data is present.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/100-days-of-code/master)


### Day 15: Feb 1, 2018

- Assignment 4 50% complete. Finished lecture content on Decision Trees for classification problem

**Thoughts:** Working through it. It was hard today. Work and Gym was heavy then had to plough through to get something done later.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_3_1.ipynb)

### Day 16: Feb 2, 2018

- Assignment 4 60% complete. One Hot encoding for categorical variables and some reading about sklearn decision trees

**Thoughts:** Working through it.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_3_1.ipynb)


### Day 17: Feb 3, 2018

- Assignment 4 99% complete. Finished making decision trees and calculating error metrics for the same.
- TODO: need to fix a big in spliting the train and validation data for assignment.

**Thoughts:** It was fun to see how I can easily play with Decision Trees and visualise them using graphviz.

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_3_1.ipynb)


### Day 18: Feb 4, 2018

- Assignment 5 50% complete for building my own decision tree algorithm to get a better understanding.
- Also fixed the splitting of training and val data for assignment 1

**Thoughts:** Visualisation of a making of Decision Tree looks much like KD-Trees. Also implementing simple version of decision tree gives a deeper intuition of what might be happening inside the model and how i can understand a leaf is formed and do feature engineering to change it for lower error

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_3_2.ipynb)


### Day 19: Feb 5, 2018

- Assignment 2 week 3 completed.
- Completed the associated quiz to work verify results.

**Thoughts:** Trying the experiment of working in the morning instead of night after work. Feels good to do it in the morning. Lets see how sustainable this is :)

**Link to work:** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nehiljain/uw_ml.git/master?filepath=classification%2Fweek_3_2.ipynb)



### Day 20: Feb 6, 2018

- Week 4 : Decision Tree overfitting strategies started. Still working through lectures
- WIP: Numpy library tutorial to understand np.array and the fundamentals better

**Thoughts:** Some libraries need special attention and love. Numpy is high on my list because it can improve speed and memory performance of python lists in my code.

**Link to work:** Still to come.

### Day 22: Feb 8, 2018

- Numpy work continues. Learnt about access and reshaping arrays.

**Thoughts:** Some libraries need special attention and love. Numpy is high on my list because it can improve speed and memory performance of python lists in my code. Its already proving useful in my data analysis work to know about numpy arrays.

**Link to work:** Still to come.
