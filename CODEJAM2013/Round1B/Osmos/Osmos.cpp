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
 
void print(std::vector<long long>  &v){
    string result ="";
    int n = v.size();
    for (int i=0;i<n;i++) {
        if (i!=(n-1)) result+= (to_string(i)+" ");
        else result+=to_string(i);        
    }
    std::cout<<result<< std::endl;
}
 

 
long long solve_subgroup(long long ref, vector<long long> &lista){
    bool bandera;
    long long aux_ref = 0;
    long long cnt;
    long long n = lista.size();

    rep(i,0,n){
        if (ref>lista.at(i)){
            ref+=lista.at(i);
        }
        else{
            bandera = true;
            cnt = 0;
            aux_ref = ref;
            while(bandera){
                aux_ref = (aux_ref*2)-1;
                cnt+=1;
                if(aux_ref>lista.at(i)){
                    bandera=false;
                }
            }
            vector <long long> sub_list (lista.cbegin()+i+1,lista.cbegin()+n);
            //cout<<lista.at(i)<<" sublist : ";
            //print(sub_list);
            //cout<<lista.at(i)<<" "<<aux_ref+lista.at(i)<<endl;
            return min(cnt+solve_subgroup(aux_ref+lista.at(i),sub_list),n-i);
        }
    }
    return 0;

}

long long solve(){    
    
    long long ref,aux;
    long long n;
    vector <long long> lista;
    cin>>ref>>n;

    rep(i,0,n) {
        cin>>aux;
        lista.push_back(aux);
    }
    if (ref==1) return (long long) n;

    sort(lista.begin(),lista.end());


    return min(solve_subgroup(ref,lista),n);
}

int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    long long  ans;
    int t;

    cin>>t;

    rep(i,0,t){
        ans = solve();
        if (i!=(t-1)){cout<<"Case #"<<i+1<<": "<< ans<<"\n";}
        else {cout<<"Case #"<<i+1<<": "<< ans; }
    }    
}

