#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    // while(num2>0  && num5>0 && num6>0)
    // {
    //     sum=sum+256;
    //     num2--;
    //     num5--;
    //     num6--;
    // }
    // while(num3>0 && num6>0)
    // {
    //     sum=sum+36;
    //     num3--;
    //     num6--;
    // }
    //cout<<sum;2 3 5 6
    cout<<min(a,min(c,d))*256+min(b,a-min(a,min(c,d)))*32;
    return 0;
}
