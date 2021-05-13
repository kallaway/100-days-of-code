#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k,d;
        cin>>n>>k>>d;
        int arr[n];
        int sum=0;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            sum=sum+arr[i];
        }
        if(sum<k)
        {
            cout<<0<<endl;
        }
        else
        {
            int x=sum/k;
            if(x>=d)
            {
                cout<<d<<endl;
            }
            else{
                cout<<x<<endl;
            }
        }
        
        
    }
    return 0;
}
