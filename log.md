# 100 Days Of Code - Log

### Day 1: 5 December, 2020

**Today's Progress**: Created a Gatsby project for my portfolio using the hello world starter theme.

**Thoughts:** Gatsby is still very new to me. I am figuring out the project file stucture and testing out different themes. Started the tutorial by CodeAddict "Gatsby - Strapi portfolio"  https://www.youtube.com/watch?v=asB-dUwpH4Y. Learning to use React custom hooks for the first time.

### Day 2: 6 December, 2020

**Today's Progress**: Continue working on my internship task the Talent Profile page. Completed components: Linked Accounts, User Details, Address. Almost finished working on the Nationality component but unable to continue due to issues with microservices not responding.

**Thoughts:** The Microservices within the project keeps closing unexpectedly and it is creating problems with debugging/testing. I have tried clean/rebuild in visual studio and close and restarting the npm server. 

### Day 3: 7 December, 2020

**Today's Progress**: Internship task. Completed Nationality component which allows talents to set their nationality. Starting working on the Languages component

**Thoughts:** Languages component requires tables, input text form, input option form, semantic buttons, semantic icons. Looking into semantic grids to format the components nicely

### Day 4: 8 December, 2020

**Today's Progress**: Made some good progress on the Languages component. I have the UI components working but cannot figure out why it is either not saving or fetching from the Database

**Thoughts:** It is proving to be more difficult than i originally thought. I may have to start this component from scratch.

### Day 5: 9 December, 2020

**Today's Progress**: Continue working on the languages component

**Thoughts:** Issues with saving languages to the Db. The function addLanguage() has null ID values after first language has been saved

### Day 5: 10 December, 2020

**Today's Progress**: Fixed the backend code for languages component 

### Day 6: 11 December, 2020

**Today's Progress**: Completed the languages component. There is a bug when saving a new language to the database for the first time, the ID's are saved as NULLs. After the component is refreshed, the language objects functions as normal. TODO: Look into solution

**Thoughts:** Working on the the next task - Skills component

### Day 7: 13 December, 2020

**Today's Progress**: Skills component on hold for now while i am thinking of good code design. Working on Visa status component

**Thoughts:** Completed Visa stats component. The CSS styling took me a while to figure out. Initially i used inline css style on the header's to space out the dropdown box. Looked into semantic ui Grids to evenly space-out the columns. Used CSS class "ui right floated teal button" to move the button to the right.

### Day 8: 15 December, 2020

**Today's Progress**: Completed job seeker status component

**Thoughts:** It took me a while to figure out why the avaiable date event handler wasn't working. It was because i forgot to call bind() on   this.handleAvailableDateChange = this.handleAvailableDateChange.bind(this);

### Day 9: 16 December, 2020

**Today's Progress**: Started working on the Profile Photo Component. The UI is set up to the requirements of the task, but i am having trouble uploading the image to the MongoDB database.

**Thoughts:** Learnt a new technique of hiding a <input type="file"> and keep a ref to it using createRef(), then when the user clicks the image, the file input hanlder method is called

### Day 10: 19 December, 2020

**Today's Progress**: Took 2 days break due to a birthday and Christmas party. Finished the description component that allows users to add a short summary and a description about themselves.

**Thoughts:** This was a really straight forward task to complete! I still cannot figure out why i'm unable to save the image to MongoDB... looking for solutions online. Next task: Skills component that allows users to view, add and edit their skillsets

### Day 11: 20 December, 2020

**Today's Progress**: Finished the Skills component that allows users to view, add, edit, and delete their skills and competency level in the Talent profile page. Started working on the Work Experience component.

**Thoughts:** The Skills component is very similar to the Languages component, this meant that i was able to copy the languages component and change the relevant fields to suit. 

### Day 12: 21 December, 2020

**Today's Progress**: Taking a break from my project work to start working on my portfolio. Created a gatsby cloud account and generated a starter template from https://github.com/LekoArts/gatsby-starter-minimal-blog

**Thoughts:** Gatsby is a powerful static site generator that leverages React.js, I was able to get it up and running within 20mins!

### Day 13: 22 December, 2020

**Today's Progress**: Going through Gatsby tutorial by CodeAddict on youtube. Started a new project called Smooth Brew Coffe Shop, learning how to create an e-commerce website using Gatsby. 

**Thoughts:** Deployed portfolio on firebase, might look into deploying to AWS free. 

### Day 14: 24 December, 2020

**Today's Progress**: Continued on coffee shop project using Gatsby.

**Thoughts:** Netlify is an amazing tool to host static sites, it supports github continuous deployment

### Day 15: 25 December, 2020

**Today's Progress**: Christmas!!! Continued on coffee shop project using Gatsby.

**Thoughts:** I learnt how to setup my Gatsby project with Contentful headless CMS. It is very easy to use and the royalty free stock images integration was very useful when creating entries for my coffee shop. However the paid plans are very exepnsive and starts from $489 a month! 

### Day 16: 26 December, 2020

**Today's Progress**: Continued on coffee shop project using Gatsby.

### Day 17: 27 December, 2020

**Today's Progress**: Made huge progress on my coffee shop website. Added Menu Items, Product Items, Contact us section with getform, CSS styling. Looking into Snipcart for cart checkout integration 

**Thoughts:** Discovered a new javascript built in object called Set that lets you store unique values of any type. It is very useful when filtering an array of objects and you only want to unique values. Combined with Array.from() static method you can create an array from the string result of Set().

### Day 18: 28 December, 2020

**Today's Progress**: Finished my Gatsby online Coffee shop. https://github.com/rethc/smooth-brew 

**Thoughts:** TODO: CSS styling, Toast notification when users add an item to the cart, Use Material UI or Bootstrap plugin, Custom logos and icons, Look more into Snipcart and styling the modals

