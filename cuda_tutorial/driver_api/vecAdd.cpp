int main()
{
    int N = 1e6;
    size_t size = N * sizeof(float);

    // Allocate input vectors h_A and h_B in host memory
    float* h_A = (float*)malloc(size);
    float* h_B = (float*)malloc(size);

    // initialize input vectors
    for(int i = 0; i < N; i++)
    {
        h_A = 1.0f;
        h_B = 2.0f;
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
    cuModuleLoad(&CuModule, "VecAdd.ptx");

    // Allocate vectors in device memory
    CUdeviceptr d_A;
    CUMemAlloc(&d_A, size);
    CUdeviceptr d_B;
    CUMemAlloc(&d_B, size);
    CUdeviceptr d_C;
    CUMemAlloc(&d_C, size);

    // Copy vectors from host memory to device memory
    cuMemcpyHtoD(d_A, h_A, size);
    cuMemcpyHtoD(d_B, h_B, size);
