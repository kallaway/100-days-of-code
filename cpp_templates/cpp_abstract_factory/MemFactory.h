
class MemFactory 
{
    public:
        virtual getMemory(std::vector<unsigned int> dims) = 0;
        virtual getShaderMemory(std::vector<unsigned int> dims) = 0;
        virtual getTensorCoreMemory(std::vector<unsigned int> dims) = 0;

};
