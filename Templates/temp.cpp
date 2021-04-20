#include<bits/stdc++.h>

#define all(A) begin(A), end(A)
#define rall(A) rbegin(A), rend(A)
#define sz(A) int(A.size())
#define pb push_back
#define mp make_pair
#define rep(i,start,n) for(int i=(start);i<n;i++)

using namespace std;
     
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef vector <pii> vpii;
typedef vector <pll> vpll;
 

int solve(){
    return 20;
}
int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    int t,ans;
    cin>>t;

    ans = solve();
    
    rep(i,0,t){
        cout<<"Case #"<<i+1<<": "<< ans<<"\n"[i == (t-1)];
    }    
}