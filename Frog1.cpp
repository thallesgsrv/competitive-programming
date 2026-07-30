#include <bits/stdc++.h>

using namespace std;

int solve(int n, vector<int>& pedras){
    vector<int> dp(n, 0);
    dp[0] = 0;
    dp[1] = abs(pedras[1] - pedras[0]);

    for (int i = 2; i < n; i++){
        dp[i] = min(dp[i-1] + abs(pedras[i] - pedras[i-1]), dp[i-2] + abs(pedras[i] - pedras[i-2]));
    }
    return dp[n-1];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;

    if (cin >> n){
        vector<int> pedras(n);
        for(int i = 0; i < n; i++){
            cin >> pedras[i];
        }
        cout << solve(n, pedras) << "\n";
    }

    return 0;
}