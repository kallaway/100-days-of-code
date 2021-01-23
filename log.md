# 100 Days Of Code - Log

### Day 0: January 4, 2021
#####

**Today's Progress**: Got development environment setup on Laptop since I had reformatted my hard drive. Started freecodecamp tutorial.

**Thoughts:** Think I'm going to start with doing some of the FreeCodeCamp tutorials.  Web development has always been a passion of mine and I haven't every really taken time to learn it beyond basic HTML and CSS. Today I accomplished the basic HTML section.

**Link to work:**[getting started](https://github.com/ryfo18/100-days-of-code)

### Day 1: January 5, 2021
#####

**Today's Progress**: Took a little detour today and started programming my NVIDIA Jetson board.  I got the board all ran some example inferencing networks with TensorRT.

**Thoughts:** Started working on the [jetson developer guide](https://developer.nvidia.com/embedded/learn/getting-started-jetson).  Left off with working on the [example C++ code](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-example-2.md) to make my own recognition model.  Also uploaded my .vimrc to github so that I can get it to different development stations.

**Link to work:**[getting started](https://github.com/ryfo18/100-days-of-code)

### Day 2: January 6, 2021
#####

**Today's Progress**: Got the imagenet model working with my C++ example and started on a CUDA tutorial.

**Thoughts:** The imagenet C++ example was ok, but didn't give me any exposure to the CUDA API.  Now workig on [this CUDA tutorial](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) and left off on the "Memory Allocation in CUDA" section.  

**Link to work:**[cuda tutorial](https://github.com/ryfo18/100-days-of-code/tree/master/cuda_tutorial)

### Day 3: January 7, 2021
#####

**Today's Progress**: Finished the CUDA tutorial and started looking into the CUDA driver API.

**Thoughts:** Started looking at the driver API and was gettig hung up trying to figure out how kernels work in CUDA.  Some resources:

[CUDA Module Management API](https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__MODULE.html#group__CUDA__MODULE_1g366093bd269dafd0af21f1c7d18115d3)
[Driver API](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#driver-api)
[nvcc overview](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html)

### Day 4: January 8, 2021
#####

**Today's Progress**: Tried the CUDA driver API but it wasn't working.  Couldn't get it compiled with g++.  Working on the vecAdd code.

**Thoughts:** Finally got the CUDA code written and couldn't compile it with g++.  Compiled with nvcc.  It had a seg fault.  Didn't spend time debugging.  

### Day 5: January 9, 2021
#####

**Today's Progress**: Finally got the CUDA driver API code working with the vector addition kernel. 

**Thoughts:** It took a lot of work to get this going, but I finally compiled a .cubin file with kernel code and compiled the host code and ran the executable and got it to run.  Tomorrow I want to look a little more into this and see if I can create a Makefile for compilation.  I'd also like to look into more how to get g++ to work for host code.

### Day 6: January 10, 2021
#####

**Today's Progress**: Was able to compile kernel code with nvcc and then use g++ to link.

**Thoughts:** Link below to show how I was able to compile and link with g++.  Looks like cuda can only be in a shared library. Started working on the Makefile but have some work to do to get it working.  Also didn't realize that I didn't put together a .cubin file from my kernel file, so need to integrate that into the Makefile.

**References to work:**[Separate compilation of CUDA code into library](https://forums.developer.nvidia.com/t/separate-compilation-of-cuda-code-into-library-for-use-with-existing-code-base/50774/8)

### Day 7: January 11, 2021
#####

**Today's Progress**: Today just did the 2nd lesson from freeCodeCamp call "Basic CSS."

**Thoughts:** I knew most of the basic CSS as it's one of the things I've done quite a bit of.  A good refresher though and learned some new things.

### Day 8: January 12, 2021
#####

**Today's Progress**: More lessons from freeCodeCamp today. Today was "Applied Visual Design."

**Thoughts:** A lot of this was new to me.  I liked the cubic-bezier function and animation sequences to get things moving on the screen.  Very interesting.


### Day 9: January 13, 2021
#####

**Today's Progress**: Spent some time today understanding the tensorcores cuDNN code.  

**Thoughts:** I cheated some today and did real work, but it was very beneficial because I had been wanting to walk through this code and think about how we want to refactor it to move the CUDA pieces into the correct places so that we can build it.  


### Day 10: January 14, 2021
#####

**Today's Progress**: Rebuilt the lotto_picker.py tool that I use for my dynasty league.

**Thoughts:** Program went through a little bit of a redesign but in the end worked very well and now I have it saved in my git repo!


### Day 11: January 15, 2021
#####

**Today's Progress**: Pretty light day of coding and just went to freeCodeCamp and did the Accessibility training.

**Thoughts:** Will probably have to revisit this training when it's relevant, but was beneficial to understand the basics of using HTML for screen readability.


### Day 12: January 16, 2021
#####

**Today's Progress**: Worked on some templates in C++

**Thoughts:** Didn't have g++ intalled on WSL SLES 15 and couldn't find out how to install it.  Couldn't find the right repository.


### Day 13: January 17, 2021
#####

**Today's Progress**: Tried to build template class MatrixMultiply example

**Thoughts:** Got gcc-c++ installed but had some issues compiling the code.  Need to look into this more tomorrow and figure out what my syntax error is.  Will review some template examples.


### Day 14: January 18, 2021
#####

**Today's Progress**: Got the templates working for the MatrixMultiply example. Also did a singleton class example.

**Thoughts:** This took a lot more debugging that I thought it would and in the end just mostly ended up being syntax issues with my code.  Templates are confusing, but very powerful.

The singleton class was pretty self-explanatory and I was largely going off the [example here](https://refactoring.guru/design-patterns/singleton/cpp/example).


### Day 15: January 21, 2021
#####

**Today's Progress**: So there's a two-day gap here...the regular day job got in the way of the programming fun that I had been having.  Nevertheless, I don't want to give this up despite breaking the "rules." 

**Thoughts:** Spent some time looking into REST APIs and did [this training](https://www.restapitutorial.com). REST APIs are becoming a buzzword and I don't know much about them.  Really looking at what purpose they would serve for me.  That was a little dry, so just spent the rest of the time at FreeCodeCamp going through some more training.  The CSS stuff is getting advanced but not really my thing.  I find myself flying through the examples.  I'm excited to finally learn Javascript.


### Day 16: January 22, 2021
#####

**Today's Progress**: Completed the CSS training and responsive web design from freecodecamp.  Now working on the [tribute page](https://www.freecodecamp.org/learn/responsive-web-design/responsive-web-design-projects/build-a-tribute-page) solution.

**Thoughts:** Built a basic page but need to spend some more time on it figuring out how to test it.  The instructions were a little cryptic.  The tribute page is for Patrick Mahomes


