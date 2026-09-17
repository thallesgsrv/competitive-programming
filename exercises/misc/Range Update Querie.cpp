#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct lazyseg {
    vector<ll> sg, lazy;

    void init(int n) {
        sg.assign(4 * n + 1, 0);
        lazy.assign(4 * n + 1, 0);
    }

    void build(int idx, int l, int r, vector<ll>& v) {
        if (l == r) {
            sg[idx] = v[l];
            return;
        }

        int mid = (l + r) / 2;

        build(2 * idx, l, mid, v);
        build(2 * idx + 1, mid + 1, r, v);

        sg[idx] = sg[2 * idx] + sg[2 * idx + 1];
    }

    void rangeUpdate(int idx, int l, int r,
                     int ql, int qr, ll val) {

        if (qr < l || r < ql) {
            return;
        }

        if (ql <= l && r <= qr) {
            lazy[idx] += val;
            return;
        }

        int mid = (l + r) / 2;

        rangeUpdate(2 * idx, l, mid, ql, qr, val);
        rangeUpdate(2 * idx + 1, mid + 1, r, ql, qr, val);
    }

    ll query(int idx, int l, int r, int pos) {

        if (l == r) {
            return sg[idx] + lazy[idx];
        }

        int mid = (l + r) / 2;

        if (pos <= mid) {
            return lazy[idx] +
                   query(2 * idx, l, mid, pos);
        }

        return lazy[idx] +
               query(2 * idx + 1, mid + 1, r, pos);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;

    vector<ll> nums(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> nums[i];
    }

    lazyseg st;
    st.init(n);
    st.build(1, 1, n, nums);

    while (q--) {
        int type;
        cin >> type;

        if (type == 1) {
            int a, b;
            ll u;

            cin >> a >> b >> u;

            st.rangeUpdate(1, 1, n, a, b, u);
        }
        else {
            int k;
            cin >> k;

            cout << st.query(1, 1, n, k) << '\n';
        }
    }

    return 0;
}