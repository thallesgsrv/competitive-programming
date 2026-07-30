#include <bits/stdc++.h>
using namespace std;

bool solve(vector<int>& x) {
    int ans = 0;

    for (int num : x) {
        ans ^= num;
    }
    return ans != 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> x(n);
        for (int i = 0; i < n; i++) {
            cin >> x[i];
        }
        if (solve(x))
            cout << "first\n";
        else
            cout << "second\n";
    }
    return 0;
}