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


### Day 17: January 23, 2021
#####

**Today's Progress**: I think I got most of the tribute page working, but need to figure out how to run thetests.

**Thoughts:** Patrick Mahomes [codepen page](https://codepen.io/burner3224/pen/qBaGGbO).


### Day 18: January 24, 2021
#####

**Today's Progress**: Got all the test cases passing and made the Mahomes page.  Chiefs win.

**Thoughts:** Super bowl, baby!


### Day 19: January 26, 2021
#####

**Today's Progress**: Didn't get to do anything yesterday unfortunately.  Today spent some time learning about ONNX runtime and other Jetson tools. 

**Thoughts:** I think I want to try the following:

1.) Take trained model from a framework (keras).
2.) Convert to ONNX.
3.) Deploy to ONNX runtime or TensorRT.

The project is definitely something to check out: [ONNX Runtime](https://github.com/microsoft/onnxruntime).

### Day 20: January 27, 2021
#####

**Today's Progress**: Working on getting ONNX runtime going in a docker container and running the yolov4 model as demonstrated in this [NVIDIA tutorial](https://developer.nvidia.com/blog/announcing-onnx-runtime-for-jetson/#:~:text=ONNX%20Runtime%20optimizes%20models%20to,and%20control%20the%20inference%20sessions.).

**Thoughts:**  Didn't get to work on converting model to onnx and then running it with ONNX runtime, but am working on this yolov4 model identifying a kite.  Might play with it a little more tomorrow.  Also want to generate a graphic of the ONNX model as [shown here](https://github.com/onnx/tutorials/blob/master/tutorials/VisualizingAModel.md).

When running the yolov4 model, the Jetson shut off.  Probably need to do a couple things:

1.) Get a jumper so I can use a 10W power supply.
2.) Disconnect the display and login via ssh.


### Day 21: January 28, 2021
#####

**Today's Progress**: Got the yolov4 tutorial working by ssh'ing in and disconnecting the display.  Did not need a jumper.  Also trying to generate a diagram of the yolov4 graph.

**Thoughts:**  The kite example was pretty neat.  I should probably try to do a couple different images from the web in the future.  I think playing with another model from scratch would be a good idea too.

### Day 22: January 29, 2021
#####

**Today's Progress**: Took a little detour...I'm kind of all over the place.  Wanted to start looking at RabbitMQ and the examples, but couldn't get the [tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html) running (wouldn't connect).  Then started playing with Docker but wouldn't work on WSL.  Complained about some kernel errors.

**Thoughts:**  Losing some focus here.  I'm trying to make up for lost time by exploring a variety of topics...deep learning, docker, web design, and rabbitMQ.  Need to get a little more focused here.  In the end I'm just trying to explore the world of software a little more and understand the tools that are out there.  Tomorrow let's focus on docker a little more on the jetson board and see what we can do.  Can I get a couple of containers talking?


### Day 23: January 30, 2021
#####

**Today's Progress**: Was able to get my laptop dual booting with OpenSUSE Tumbleweed.  Installed rabbitmq and got the example working.  Also looked at the [Docker tutorial](https://docs.docker.com/get-started/) and watched a really good video explaining how containers worked.

**Thoughts:** It was nice to get rabbitMQ working.  The video in the docker tutorial was also very informative and taught me a lot about linux processes, chroot'ing to mount the container filesystem, and cgroups.  Tomorrow would like to take this further and get the rabbitMQ send and receive scripts running in separate containers.

### Day 24: January 31, 2021
#####

**Today's Progress**: Spent time trying to understand the [AMQP-CPP](https://github.com/CopernicaMarketingSoftware/AMQP-CPP) project to see how I can utilize it in my own code to create a sender/receiver. 

**Thoughts:** It was a little more elaborate than I thought.  I read through the documentation of the project, and just need to spend some time tomorrow hacking away to create a basic publish/send.  From there I can take some more elaborate steps to abstract everything away.

### Day 25: February 1, 2021
#####

**Today's Progress**: Not much coding today but concerned myself with the design of an interoperable OpenCL/CUDA neural network manager.

**Thoughts:** Good progress and took a lot of notes.  Need to review everything to come up with the final proposed design.

### Day 26: February 2, 2021
#####

**Today's Progress**: Dove into the Allocation classes to understand what is needed from a CuAllocation.  Ran into more questions than answer.

**Thoughts:** Need to continue working on this.  Not much coding again today but good understanding.  Need to get back to coding though.

### Day 27: February 3, 2021
#####

**Today's Progress**: Got the libuv.cpp example to compile in the amqp-cpp project and finally got it running after much debugging and issues.

**Thoughts:** I started with libev.cpp and it was complaining that it couldn't find "libev" from my Makefile.  My dumb mistake.  After trying libevent.cpp and libuv.cpp, I finally figured out it was because I was specifying "-llibuv" and I should have just been specifying "-luv."  Got it to compile.  Then the program wouldn't run.  Why?  because I had the "-c" option in g++.  This tells g++ to not run the linker, so it wasn't linking against any of the shared libraries.  After removing that, it worked.

### Day 28: February 4, 2021
#####

**Today's Progress**: Got the libev.cpp example to compile and even modified it to send messages using timer on my hello queue that were received by Docker recieve that I created.

**Thoughts:** This was a pretty successful day.  I have a C++ application talking to my talker container.  From here, I'd like to explore a little bit more into making my own class that inherits from the amqp-cpp TcpHandler and implements a montior method.
