#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
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
        int sum=0;
        for(int i=0;i<n;i++)
        {
            sum=sum+v[i];
        }
        if(sum>x)
        {
            cout<<"YES"<<endl;
            sort(v.begin(),v.end(),greater<int>());
            for(int i=0;i<n;i++)
            {
                cout<<v[i]<<" ";
            }
            cout<<endl;
        }
        else
        {
            int flag=0;
            sort(v.begin(),v.end());
           for(int i=0;i<n;i++)
           {
               if(v[i]==x)
               {
                   flag=1;
               }
               else{
                   flag=0;
               }
           }
           if(flag==1)
           {
               cout<<"NO"<<endl;
           }
        }
    }
    return 0;
}
