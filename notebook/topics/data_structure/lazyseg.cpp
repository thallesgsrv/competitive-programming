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

    void push(int idx, int l, int r) {
        if (lazy[idx] == 0) {
            return;
        }

        sg[idx] += (r - l + 1) * lazy[idx];

        if (l != r) {
            lazy[2 * idx] += lazy[idx];
            lazy[2 * idx + 1] += lazy[idx];
        }

        lazy[idx] = 0;
    }

    void rangeUpdate(int idx, int l, int r,
                     int ql, int qr, ll val) {

        push(idx, l, r);

        if (qr < l || r < ql) {
            return;
        }

        if (ql <= l && r <= qr) {
            lazy[idx] += val;
            push(idx, l, r);
            return;
        }

        int mid = (l + r) / 2;

        rangeUpdate(2 * idx, l, mid, ql, qr, val);
        rangeUpdate(2 * idx + 1, mid + 1, r, ql, qr, val);

        sg[idx] = sg[2 * idx] + sg[2 * idx + 1];
    }

    ll query(int idx, int l, int r,
             int ql, int qr) {

        push(idx, l, r);

        if (qr < l || r < ql) {
            return 0;
        }

        if (ql <= l && r <= qr) {
            return sg[idx];
        }

        int mid = (l + r) / 2;

        ll left = query(2 * idx, l, mid, ql, qr);
        ll right = query(2 * idx + 1, mid + 1, r, ql, qr);

        return left + right;
    }
};
