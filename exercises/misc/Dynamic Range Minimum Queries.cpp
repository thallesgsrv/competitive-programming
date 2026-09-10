#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<ll> nums;

struct seg {
    vector<ll> sg;

    void init(){
        sg.assign(4*n, 0);
        build(1, n, 1);
    }

    ll merge(ll left, ll right){
        return min(left, right);
    }

    void build(int l, int r, int node){
        if (l == r) {
            sg[node] = nums[l];
            return;
        }
        int mid = (l+r) / 2;
        build(l, mid, node*2);
        build(mid+1, r, node*2+1);
        sg[node] = merge(sg[node*2], sg[node*2+1]);
    }

    ll query(int l, int r, int s, int e, int node){
        if (l > e || r < s) return LLONG_MAX;
        if (s <= l && r <= e) return sg[node];
        int mid = (l+r)/2;
        return merge(
            query(l, mid, s, e, node*2),
            query(mid+1, r, s, e, node*2+1)
        );
    }

    void update(int l, int r, ll val, int id, int node){
        if (l == r){
            sg[node] = val;
            return;
        }
        int mid = (l+r)/2;
        if (id <= mid) update(l, mid, val, id, node*2);
        else update(mid+1, r, val, id, node*2+1);
        sg[node] = merge(sg[node*2], sg[node*2+1]);
    }
    
    ll query(int a, int b){ return query(1, n, a, b, 1); }
    void update(int id, ll val){ update(1, n, val, id, 1); }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    cin >> n >> q;

    nums.assign(n+1, 0);
    for (int i = 1; i <= n; i++){
        cin >> nums[i];
    }

    seg st;
    st.init();

    for (int i = 0; i < q; i++){
        int type;
        cin >> type;
        if (type == 1){
            int k; ll u;
            cin >> k >> u;
            st.update(k, u);
        } else {
            int a, b;
            cin >> a >> b;
            cout << st.query(a, b) << "\n";
        }
    }

    return 0;
}