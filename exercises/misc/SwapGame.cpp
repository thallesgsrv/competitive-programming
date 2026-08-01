#include <bits/stdc++.h>
using namespace std; 

bool solve(){
    int n;
    cin >> n;
    
    vector<int> numbers(n);
    for(int i = 0; i < n; i++){
        cin >> numbers[i];
    }

    int ans, rest;

    ans = numbers[0];
    rest = numbers[1];
    for(int i = 2; i < n; i++){
        rest = min(rest, numbers[i]);
    }
    
    if(ans > rest){
        return true;
    } else {
        return false; 
    }
} 

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        if (solve()){
            cout << "Alice\n";
        } else {
            cout << "Bob\n";
        }
    }
    return 0;
}