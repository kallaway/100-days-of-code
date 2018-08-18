#include <iostream>
#include<bits/stdc++.h>
#include<math.h>
#include<vector>
using namespace std;
 
int main() {
	long int i,j;
	vector<long long int>b;
	
	vector<long int>a(100000,0);
	for(i=0;i<100000;++i)
        {a[i]=i;}
    
	for(i=0;i<100000;++i)
	{
		j=a[floor(i/3)]+a[floor(i/2)]+a[floor(i/4)];
		if(j>i){a[i]=j;}
	}
	
	long long int t,s,x,y,z;
	
	while(cin>>t){
	s=0;	
	int l=0;
	b.push_back(t);
	while(l>=0)
	{
		if(b[l]>100000)
        {t=b[l];	
        b.pop_back();
        x=floor(t/3);
		y=floor(t/2);	
		z=floor(t/4);	
		b.push_back(x);
		b.push_back(y);
        b.push_back(z);
        l+=2;
        }
		else{
                s+=a[b[l]];	b.pop_back();	--l;}
			}
	cout<<s<<"\n";
	b.clear();
	}
	return 0;
} 
