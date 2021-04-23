#include<bits/stdc++.h>
using namespace std;
void isprime(int a,int b)
{
    int check=1;
    int check2=1;
    if(a<2 || b<2)
    {
        cout<<"NO"<<endl;
    }
    for(int i =2;i<a;i++)
    {
        if(a%i==0)
        {
            check=0;
        }
    }

    for(int i =2;i<b;i++)
    {
        if(b%i==0)
        {
            check2=0;
        }
    }
    if(check==0 || check2==0)
    {
        cout<<"NO"<<endl;
        
    }
    vector<int>v;
    if(check==1 && check2==1)
    {
        for(int num=a ;num<=b;num++)
        {
            int i;
            for( i=2;i<num;i++)
            {
                if(num%i==0)
                {
                    break;

                }
                
            }
            if(num==i)
            {
                v.push_back(num);
            }
        }
    }
    for(int i=0;i<v.size();i++)
    {
        if(v[i]==a && v[i+1]==b)
        {
            cout<<"YES";
        }
        
        else
        {
            cout<<"NO";
        }

    }

}
int main()
{
    int n,m;
    cin>>n>>m;
    isprime(n,m);
    return 0;
}
