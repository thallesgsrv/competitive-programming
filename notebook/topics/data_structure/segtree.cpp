#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<ll> nums;

struct seg{
    vector<ll> sg;
    void init() {
        sg.resize(4*n);
        build(1, n, 1);
    }
    ll merge(ll left, ll right){
        return left + right;
    }
    void build(int l, int r, int node){
        if(l == r){
            sg[node] = nums[l];
            return;
        }
        int mid = (l+r) / 2;
        build(l, mid, node*2);
        build(mid+1, r, node*2+1);
        sg[node] = merge(sg[node*2], sg[node*2+1]);
    }
    ll query(int l, int r, int s, int e, int node){
        if(l > e || r < s) return 0;
        if(s <= l && r <= e) return sg[node];
        int mid = (l+r)/2;
        return merge(
            query(l, mid, s, e, node*2),
            query(mid+1, r, s, e, node*2+1)
        );
    }
    void update(int l, int r, ll val, int id, int node) {
        if(l == r){
            sg[node] = val;
            return;
        }
        int mid = (l+r)/2;
        if(id <= mid) update(l, mid, val, id, node*2);
        else update(mid+1, r, val, id, node*2+1);
        sg[node] = merge(sg[node*2], sg[node*2+1]);
    }
};