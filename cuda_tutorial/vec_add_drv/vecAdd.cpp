#include <cuda.h>
#include <stdio.h>
#include <math.h>


int main()
{
    int N = 1e6;
    size_t size = N * sizeof(float);

    // Allocate input vectors h_A and h_B in host memory
    float* h_A = (float*)malloc(size);
    float* h_B = (float*)malloc(size);
    float* h_C = (float*)malloc(size);

    // initialize input vectors
    for(int i = 0; i < N; i++)
    {
        h_A[i] = 1.0f;
        h_B[i] = 2.0f;
    }

    // Initialize -- this must always be called
    cuInit(0);

    // Get number of devices supporting CUDA
    int deviceCount = 0;
    cuDeviceGetCount(&deviceCount);
    if(deviceCount == 0)
    {
        printf("There is no device supporting CUDA.\n");
        exit(0);
    }

    // Get handle for device 0
    CUdevice cuDevice;
    cuDeviceGet(&cuDevice, 0);

    // create context
    CUcontext cuContext;
    cuCtxCreate(&cuContext, 0, cuDevice);

    // Create module from binary file
    CUmodule cuModule;
    cuModuleLoad(&cuModule, "vecAdd_kernel.cubin");

    // Allocate vectors in device memory
    CUdeviceptr d_A;
    cuMemAlloc(&d_A, size);
    CUdeviceptr d_B;
    cuMemAlloc(&d_B, size);
    CUdeviceptr d_C;
    cuMemAlloc(&d_C, size);

    // Copy vectors from host memory to device memory
    cuMemcpyHtoD(d_A, h_A, size);
    cuMemcpyHtoD(d_B, h_B, size);

    // Get function handle from module
    CUfunction vecAdd;
    cuModuleGetFunction(&vecAdd, cuModule, "vecAdd_kernel");

    // Invoke kernel
    int threadsPerBlock = 256;
    int blocksPerGrid= (N + threadsPerBlock - 1) / threadsPerBlock;

    void* args[] = { &d_A, &d_B, &d_C, &N };
    cuLaunchKernel(vecAdd, blocksPerGrid, 1, 1, threadsPerBlock, 1, 1, 0, 0, args, 0);

    cuMemcpyDtoH(h_C, d_C, size);

    // Verify result
    int i;

    float maxErr = 0.0f; 
    for(i = 0; i < N; i++)
    {
        maxErr = fmax(maxErr, fabs(d_C - 3.0f));
    }

    printf("Max Error %f", maxErr);

    cuMemFree(d_A);
    cuMemFree(d_B);
    cuMemFree(d_C);

    delete [] h_A;
    delete [] h_B;
    delete [] h_C;
}
