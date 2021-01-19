#include "MatrixMultiply.h"
#include <iostream>
#include <math.h>

template<typename T>
MatrixMultiply<T>::MatrixMultiply(size_t size) : m_size(size) 
{
	m_result = new T[size];
}

template<typename T>
MatrixMultiply<T>::~MatrixMultiply()
{
	delete [] m_result;
}

template<typename T>
T* MatrixMultiply<T>::execute(T *mul1, T *mul2)
{
	for(int i = 0; i < m_size; i++)
	{
		m_result[i] = mul1[i] * mul2[i];
	}

	return m_result;
}


int main()
{
	const int size = 1e6;
	const float exp_result = 2.0f;
	float* x = new float[size];
	float* y = new float[size];

	for(int i = 0; i < size; i++)
	{
		x[i] = 2.0f;
		y[i] = 1.0f; 
	}	

	MatrixMultiply<float> mul(size);
	float* result;
	result = mul.execute(x, y);
	
	float maxdiff = 0.0f;
	for(int i = 0; i < size; i++)
	{
		maxdiff = fmax(maxdiff, (result[i] - exp_result));
	}
	
	std::cout << "Max difference is " << maxdiff << std::endl;

	delete [] x;
	delete [] y;
	
}

