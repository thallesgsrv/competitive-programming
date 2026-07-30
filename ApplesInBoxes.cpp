#include <bits/stdc++.h>
using namespace std;

string solve(vector<long long>& a, long long k) {
    long long sum = 0;
    long long mx = 0;
    long long mn = LLONG_MAX;

    for (long long x : a) {
        sum += x;
        mx = max(mx, x);
        mn = min(mn, x);
    }

    long long dif = mx - mn;

    long long cntMax = 0;
    for (long long x : a) {
        if (x == mx)
            cntMax++;
    }

    if (dif > k + 1) {
        return "Jerry";
    }

    if (dif <= k) {
        return (sum % 2 ? "Tom" : "Jerry");
    }

    if (cntMax > 1) {
        return "Jerry";
    }

    return ((sum - 1) % 2 == 0 ? "Tom" : "Jerry");
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        long long k;

        cin >> n >> k;

        vector<long long> a(n);

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        cout << solve(a, k) << '\n';
    }

    return 0;
}