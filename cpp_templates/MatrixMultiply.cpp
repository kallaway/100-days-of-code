#include "MatrixMultiply.h"

template<class T>
MatrixMultiply::MatrixMultiply(size_t size) : m_size(size) 
{
	m_result = new T[size];
}

MatrixMultiply::~MatrixMultiply()
{
	delete [] m_result;
{

T execute(T mul1, Tmul2)
{
	T result = 0;
	for(int i = 0; i < m_size; i++)
	{
		result[i] = mul1[i] * mul2[i];
	}

	return result;
}


int main()
{
	const int size = 1e6;
	const float exp_result = 2.0f;
	float x = new float[size];
	float y = new float[size];

	for(int i = 0; i < size; i++)
	{
		x[i] = 2.0f;
		y[i] = 1.0f; 
	}	

	MatrixMultiply mul(size);
	float result;
	result = mul.execute(x, y);
	
	float maxdiff = 0.0f;
	for(int i = 0; i < size; i++)
	{
		maxdiff = max(maxdiff, (result[i] - exp_result);
	}
	
	std::cout << "Max difference is " << maxdiff << std::endl;
	
}

