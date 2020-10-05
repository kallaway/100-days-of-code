# 100 Days Of Code - Log


### Day 2:  Oct 2, 2020 


**Today's Progress**: Reviewing my TechJobsPersistent project for the flow, presentation, and relationships of data and views.

**Thoughts/Notes/Braindump space:**   
  *What I like:*  
       1- I created a list by category section that will list every item added (employer and skill).
       2- When I add a new job, I can add name and select which employer.  
            A- I would like to have this for my parent user to select which child the book will be assigned to (if multiple children signed up)
            B- there is also an option to add tags, which could also be used to select if fiction, non-fiction, chapter book, (or whatever they want to add)  
        3- There is a Skill option that allows the user to create tags to then group books by the similar tags.
            - this could be great for grouping books based on genre or type (see 2-B)
        

**Pre-Build Space -->**  *parts review* -
        
        
        1- Home (Controller and Views ONLY)
              A- CONTROLLER 
                  i- uses both jobContext and ID with private set
                  ii- HttpGet Index()
                      a- creates List of Jobs using context and referring to an lambda that pulls the Employer  **Look into the Job Model**
                      b- returns view of the list on the index
                  iii- HttpGET Add()
                      a.  uses the AddJobVM and Employers to build the list on the Index Page  
                      **THIS IS WHAT I AM LOOKING FOR**
                  iv- HttpPOST ProcessAddJobForm()
                      a.  takes both AddJbVM and a string[] of JobSkills to fill a table
                          1- creates a job object that pulls data from 2 sources
                                A- addJobVM.Name and addJobVM.EmployerId
                                B- JobSkills are created in a new List of JobSkill Objects
                          2- then there is FOREACH loop to find the job skills associated with each new job object we created (See 1.A.iv.1.B above) Adding them to the job object
                          3.  We update the table by saving changes and we return to the Home Index View OR Add Job View if we're missig a step  (Validation)
                  v. Detail()
                      a. creating new objects to display on the index page (theJob and jobSkills)
                      uses the new Job object's id to create the list
                          i- we pull out the employer, and the id for the job title presentd
                          ii - We sort through the list of Jobsklls objects for the skills we want
                              a- find the skill Id, make sure to bring the skills along and then add to a list  
                           iii- call to the JobDetailVM to present theJob and jobSkills and return that viewmodel
             B- VIEWS (Index, Detail, AddJob)
                 1- INDEX
                    a- using the List of Job objects
                    b- calling our controllers as "buttons" to open other views
                    c- TABLE
                        i- Using the Model Count to initiate table
                        ii- table created with Job Name and Employer Name
                            a- looking for the Job in the Model (as called from the list)
                                1. Using the DETAIL action on the HOME Controller, find the id and Name
                   2-DETAIL
                        a- using the JobDetailVM
                        b- Using the acutal Models to full in the Name and text in TABLE
                        c- Option to add skills to this particular job, pulls on the JobId for its route
                        There are checkboxes AND DD on this view.  I like the idea of both.  See how they are built.
                           
          
        2- Employer (controller, views, model, viewmodel)
              A- CONTROLLER
                  i-dbContext, has Employer DbSet in the data folder
                  ii- HttpGet Add() - uses VM to present form for user 
                  iii- HttpPost ProcessAddEmployerForm() - renamed Add fucntion
                         a- pulls name and location from VM, and redirects to Employer index view
                         **b- I don't understand like 56**
                  iv- About() - uses id and Employer context to find the selected employer
                        a- in the view, you can select the name of the employer and it will take you to a view that has only the info about that employer 
                        b- used in the LIST view
                              1- the spacing in this view could be better -
                              
                B- VIEWMODEL (AddEmployerViewModel)
                    i- Validation for each Item
                    ii- collecting Name and Location only
                    
                C- MODEL
                    i- Contains Id, Name, Location
                    ii- Default constructor AND loaded constructor
                    
                D - VIEW (About, Add, Index)
                    i- ABOUT 
                        a- pulling Employer using Model.Name
                        b- Listing Name and Location
                        c- simple heading a p tags
                    ii- ADD
                        a- this one uses the validation that was created in the ViewModel
                        b- collecting Name and Location (exactly what was in both Model and VM)
                    iii- INDEX
                        a- This has a table that is filled based on employers created
                            1- I wonder if I could play around with this table to practice my Book/RL 
          3- 
**AND BREAK FOR LUNCH WITH THE CHICKADEES**


**Post-Build Space: -->**  

Not able to get back to project.  But did learn about what features I want, and have a better understanding of calling between views and contollers.

**Link to work:** https://github.com/speudusa/OPM && https://github.com/speudusa/TechJobsMOREPersistent


**------------------------------------------------------**



### Day 1:  Oct 1, 2020

**Today's Progress**: Building One Page More

**Thoughts/Notes/Braindump space:**   

**Pre-Build Space -->** The Reading List (RL) can exist without the Book (B) objects.  RL is basically a shelf to display things, anything really, books, people, rotary phones, etc.  The shelf can exist without the book in this context.  The B can not exist without the shelf (they would be floating like fruit in a jello ring.  We need to bring jello rings back.)

Okay, so now that I better understand this relationship, I see how I need to incorporate the ORM and collections.  

**Post-Build Space -->**  So, don't get mad.  I added Users instead.  This made a lot of sense with the section of the book I was reading.  While I was trying to figure out how to build the Book/RL relationship, the set up in the book made the most sense here.  Parent can add child AND book, but can now assign book to specific child (I hope)

(having a hard time testing this right now since I didn't finish my inital task and that is full of errors preventing me from running it, BUT in spirit I think it is a good start)

**Link to work:**  https://github.com/speudusa/OPM

**------------------------------------------------------**

### Day 0: Oct 1, 2020


**Today's Progress**: I did code, but I wanted to set my intention and create a space for me to work through my blocks.  This Project is my final project for LaunchCode's LiftOff.  It is the (first) and biggest thing I have ever build on my own.  I am trying to make space for it in my day to day life, and hope that creating a place to plan, ponder, and grow from will be more helpful than just a list of Ta-Da's!  For me.  

I added a place to drop things.  I added space to list my goal for the day and a place to list where I stopped.  But these spaces are also places that can hold more than just facts and figures, but the story behind it all, the place when connections are made.  So, if you want to read along, you are welcome to.  I will try to keep these updates short and to the point.  

I should make a parking lot...  but not here.  

**Thoughts/Notes/Braindump space:** 

**Pre-Build Space -->**  Rethink my process.  How do I best learn?  Stories, writing about it, making connections.

**Post-Build Space: -->**  So, here is my redesigned log.  My rekindled passion to make this project happen.  

**Link to work:**  https://github.com/speudusa/OPM

**------------------------------------------------------**

**------------------------------------------------------**

### Day 0: TEMPLATE


**Today's Progress**: 

**Thoughts/Notes/Braindump space:** 

**Pre-Build Space -->**  

**Post-Build Space: -->**

**Link to work:**

**------------------------------------------------------**
