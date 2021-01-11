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
