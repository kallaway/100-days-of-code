#include<iostream>
#include<bits/stdc++.h>
#define _test   int _TEST; cin>>_TEST; while(_TEST--)
#define int long long
const int N = 100100;
using namespace std;
int32_t main(){
int t;
cin>>t;
while(t--){
    int n;
    cin>>n;
    string s;
    cin>>s;
    vector<int>v;
    int prev = 'a';
    int count=0;
    // we begin with smallest ,just in ints
    for(int i =n-1;i>=0;i--){
        if(s[i]>=prev){
            // their inddices
            v.push_back(i);
            prev=s[i];

        }
    }
    // prev me sabse bada jo hai vo hai
    // ab hum uske count ko store karege 
    // aur use v me se remove karege
    for(int i =0;i<n;i++){
        if(prev == s[i]){
            count++;
        }
    }
    int m  =v.size();
    // size of larget subsequence
    // after storing their indices we swp them
    for(int i =0;i<m/2;i++){
        swap(s[v[i]],s[v[m-i-1]]);
    }
    int ans = v.size()-count;
    // now e check if sorteed or not
    for(int i =1;i<n;i++){
        if(s[i]<s[i-1]){
            ans = -1;
            break;
        }
    }
    cout<<ans<<endl;
}	
    return 0;
}