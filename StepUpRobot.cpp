#include <bits/stdc++.h>
using namespace std;

string solve(int x, int n, int m, vector<int>& degraus, vector<int>& armadilhas) {
    vector<bool> is_trap(x + 1, false);
    for (int b : armadilhas) {
        if (b <= x) {
            is_trap[b] = true;
        }
    }
    vector<bool> dp(x + 1, false);
    dp[0] = true;


    for (int i = 1; i <= x; i++) {
        if (is_trap[i]) {
            dp[i] = false;
            continue;
        }

        for (int pulo : degraus) {
            if (i - pulo >= 0 && dp[i - pulo]) {
                dp[i] = true;
                break;
            }
        }
    }
    
    return dp[x] ? "Yes" : "No";
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;

    if (cin >> n){
        int m;
        vector<int> degraus(n);

        for (int i = 0; i < n; i++){
            cin >> degraus[i];
        }
        if (cin >> m){
            vector<int> armadilhas(m);

            for (int i = 0; i < m; i++){
            cin >> armadilhas[i];
        }
        int x;
        cin >> x;
        cout << solve(x,n,m,degraus,armadilhas) << "\n";
        }
    }
}