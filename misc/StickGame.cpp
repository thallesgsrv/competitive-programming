#include <bits/stdc++.h>
using namespace std;

string solve(int n, vector<int>& jogadas){
    vector<bool> dp(n+1, false);

    for (int i = 1; i <= n; i++){
        for (int j : jogadas){
            if (i >= j && !dp[i-j]){
                dp[i] = true;
                break;
            }
        }
    }

    string ans;

    for (int i = 1; i <= n; i++){
        ans += (dp[i] ? 'W' : 'L');
    }

    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;

    if(cin >> n >> k){
        vector<int> jogadas(k);
        for(int i = 0; i < k; i++){
            cin >> jogadas[i];
        }
        cout << solve(n,jogadas) << "\n";
    }
}