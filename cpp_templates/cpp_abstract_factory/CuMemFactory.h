
#include "MemFactory.h"

class CuMemFactory : MemFactory
{
    public:
        CuMemFactory();
        ~CuMemFactor();

        void getMemory(std::vector<unsigned in> dims)
        {
            return new CuBuffer();
        }
        void getShaderMemory(std::vector<unsigned int> dims)
        {
            return new CuShader();
        }
        void getTensorCoreMemory(std::vector<unsigned int> dims)
        {
            return new CuTensorCore
        }
        

};
