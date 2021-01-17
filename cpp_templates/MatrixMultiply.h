

template<class T>
class MatrixMultiply
{
	MatrixMultply(size_t size);
	~MatrixMultiply() {};

	T execute(T mul1, T mul2);

	private:
		int m_size;
		T m_result;
{
