#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;
        cin>>n>>x;
        vector<int>v;
        for(int i=0;i<n;i++)
        {
            int y;
            cin>>y;
            v.push_back(y);
        }
        int y=0;
        for(int i=0;i<v.size();i++)
        {
            if(v[0]>x)
            {
                y=1;
            }
        }
        if(y==1)
        {
            cout<<"YES"<<endl;
        }
        
        sort(v.begin(),v.end());
        int sum=0;
        for(int i=0;i<v.size();i++)
        {
           while(sum<=x)
           {
               sum=sum+v[i];
           }
        }
        if(sum==x)
        {
            sort(v.begin(),v.end(),greater<int>());
            cout<<"YES"<<endl;
            for(auto i:v)
            {
                cout<<i<<" ";
            }
        }
        
        int flag=0;
        for(int i=0;i<v.size();i++)
        {
            if(v[i]==x)
            {
                flag=1;
            }
            else
            {
                flag=0;
            }
            
            
        }
        if(flag==1)
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
