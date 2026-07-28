#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 +7;

int solve(int n, vector<int>& dp){
    dp[0] = 1;

    for(int i = 1; i <= n; i++ ){
        for(int j = 1; j <= 6; j++){
            if (i-j >= 0){
                dp[i] = (dp[i] + dp[i-j]) % MOD; 
            }
        }
    }
    return dp[n];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if(cin >> n){
        vector<int> dp(n+1, 0);

        cout << solve(n, dp) << "\n";
    }
    return 0;
}