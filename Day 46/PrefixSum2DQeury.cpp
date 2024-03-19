#include<iostream>
#include<bits/stdc++.h>
#define pll = pair<ll, ll>
#define tlll = tuple<ll, ll, ll>
#define _test   int _TEST; cin>>_TEST; while(_TEST--)
#define int long long
#define dis(x) cout<<x<<endl
#define pb push_back
#define pp pop_back
#define mp make_pair
#define ff first
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define ASST(x,y,z) assert(x >= y && x <= z)
#define ss second
#define rep(i,a,n) for(int i = (a); i <= (n); ++i)
#define sz(a) (int)(a.size())
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
const int N = 100100;
using namespace std;
    //     vector<vector<int> > a(N, vector<int>(N, 0));
    // vector<vector<int> > pf(N, vector<int>(N, 0));
    // int a[N][N];
// int pf[N][N];
int32_t main(){
int n;
cin>>n;
    vector<vector<int> > a(n + 1, vector<int>(n + 1, 0));
    vector<vector<int> > pf(n + 1, vector<int>(n + 1, 0));
for(int i =1;i<=n;++i){
    for(int j =1;j<=n;++j){
        cin>>a[i][j];
        pf[i][j] += a[i][j] + pf[i-1][j] + pf[i][j-1] -pf[i-1][j-1];
    }
}	
for(int i =1;i<=n;++i){
    for(int j =1;j<=n;++j){
        cout<<pf[i][j]<<" ";
    }
    cout<<endl;
}
int q;
cin>>q;
while(q--){
    int x1, y1, x2, y2;
    cin>>x1>>y1>>x2>>y2;
    cout<<pf[x2][y2] - pf[x1-1][y2] - pf[x2][y1-1] + pf[x1-1][y1-1];
}
return 0;
}
