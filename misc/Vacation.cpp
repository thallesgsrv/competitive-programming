#include <bits/stdc++.h>
using namespace std; 

int solve(int n,const vector<int>& a,const vector<int>& b,const vector<int>& c){
    vector <vector<int>> dp(n+1, vector<int>(3,0));
    dp[1][0] = a[1];
    dp[1][1] = b[1];
    dp[1][2] = c[1];

    for (int i = 2; i <= n; i++){
        dp[i][0] = a[i] + max(dp[i-1][1], dp[i-1][2]);
        dp[i][1] = b[i] + max(dp[i-1][0], dp[i-1][2]);
        dp[i][2] = c[i] + max(dp[i-1][0], dp[i-1][1]);
    }
    return max({dp[n][0], dp[n][1], dp[n][2]});
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;  

    if (cin >> n){
        vector<int> a(n+1), b(n+1), c(n+1);
        for (int i = 1; i <= n; i++){
            cin >> a[i] >> b[i] >> c[i];
        }
        cout << solve(n, a,b ,c) << "\n";
    }
    return 0;
}