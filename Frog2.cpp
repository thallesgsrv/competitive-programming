#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int solve(int n, int k, vector<int>& pedras){
    vector<int> dp(n, INF);

    dp[0] = 0;

    for (int i= 1; i < n; i++){
        for (int j=1; j<=k; j++){
            if (i-j>=0){
                dp[i] = min(dp[i], dp[i-j] + abs(pedras[i] - pedras[i-j]));
            }
        }
    }
    return dp[n-1];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;

    if (cin >> n >> k){
        vector<int> pedras(n);
        for (int i = 0; i<n ; i++){
            cin >> pedras[i];
        }
        cout << solve(n ,k ,pedras) << "\n";
    }
    return 0;
}