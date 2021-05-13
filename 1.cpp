#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll  a,b,c;
        cin>>a>>b>>c;
        if(a>c)
        {
            cout<<-1<<" "<<4<<endl;
        }
        else if(c>a){
            if(c/b >= a)

            {
                cout<<4<<" "<<-1<<endl;
            }
            else{

            }
        }
    }
    return 0;
}
