#include <iostream>
using namespace std;
int main(){
	int a;
	int b;
	cout<<"enter the value of a and b"<<endl;
	cin>>a>>b;
	if(a>b){
		cout<<"a is greater"<<endl;
	}
	else if(b>a)
	{
		cout<<"b is greater"<<endl;
	}
	else
		cout<<"both are equal"<<endl;
	return 0;
}
