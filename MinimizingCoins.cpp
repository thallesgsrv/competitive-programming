#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;

int solve(int x, vector<int>& dp, const vector<int>& moedas){
    dp[0] = 0;
    for (int i = 1; i <= x; i++){
        for (int c : moedas){
            if(i-c >= 0){
                dp[i] = min(dp[i], dp[i-c]+1);
            }
        }
    }
    if (dp[x] == INF){
        return -1;
    }
    return dp[x];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;

    if (cin >> n >> x){
        vector<int> moedas(n);
        for (int i = 0; i < n; i++){
            cin >> moedas[i];
        }
        vector<int> dp(x+1, INF);
        cout << solve(x,dp, moedas) << "\n";
    }
    return 0;
}