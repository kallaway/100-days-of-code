CUDA_PATH ?= /usr/local/cuda-10.2

INCLUDES += $(CUDA_PATH)/include 
LIB_PATH += $(CUDA_PATH)/lib64
LIBS += lcudart lcuda

HOST_COMPILTER ?= g++
NVCC = $(CUDA_PATH)/bin/nvcc -ccbin $(HOST_COMPILER)

# internal flags
NVCCFLAGS := -m64
CCFLAGS :=
LDFLAGS :=

# device architecture flags
GENCODE_FLAGS ?= -arch=sm_53

EXEC ?= @echo "[@]"

vecAdd_kernel.o: vecAdd_kernel.cu
	$(EXEC) $(NVCC) $(GENCODE_FLAGS) $(NVCCFLAGS) -dc -o $@

vecAdd_kernel.dlink.o: vecAdd_kernel.o
	$(EXEC) $(NVCC) $(GENCODE_FLAGS) $(NVCCFLAGS) -dlink -o $@

vecAdd_kernel.a: vecAdd_kernel.dlink.o vecAdd_kernel.o
	$(EXEC) $(NVCC) $(GENCODE_FLAGS) $(NVCCFLAGS) -lib -o vecAdd_kernel.a

vecAdd.o: vecAdd.cpp
	$(HOST_COMPILER) $(INCLUDES) -o $@

vecAdd: vecAdd.o vecAdd_kernel.a
	$(HOST_COMPILER) -o $@ $(LIB_PATH) $(LIBS)

