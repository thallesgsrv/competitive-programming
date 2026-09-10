#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<int> nums;

struct seg{
    vector<pair<int,int>> sg;

    void init(){
        sg.assign(4*n, {0,0});
        build(1, n, 1);
    }

    pair<int,int> merge(pair<int,int> a, pair<int,int> b){
        return (a.first >= b.first) ? a : b;
    }

    void build(int l, int r, int node){
        if (l == r){
            sg[node] = {nums[l], l};
            return;
        }
        int mid = (l+r) / 2;
        build(l, mid, node*2);
        build(mid+1, r, node*2+1);
        sg[node] = merge(sg[node*2], sg[node*2+1]);
    }

    pair<int,int> query(int l, int r, int s, int e, int node){
        if (l > e || r < s) return {0, 0};
        if (s <= l && r <= e) return sg[node];
        int mid = (l+r) / 2;
        return merge(
            query(l, mid, s, e, node*2),
            query(mid+1, r, s, e, node*2+1)
        );
    }

    pair<int,int> query(int a, int b){
        return query(1, n, a, b, 1);
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    cin >> n >> q;

    nums.assign(n+1, 0);
    for (int i = 1; i <= n; i++) cin >> nums[i];

    seg st;
    st.init();

    string out;
    out.reserve(q * 12);

    for (int i = 0; i < q; i++){
        int L, R;
        cin >> L >> R;

        auto [maxVal, pos] = st.query(L, R);
        (void)maxVal;

        bool adilsonWins;
        if (pos == L || pos == R){
            adilsonWins = true;
        } else {
            int len = R - L + 1;
            adilsonWins = (len % 2 == 0);
        }

        out += (adilsonWins ? "Adilson" : "Reginaldo");
        out += '\n';
    }

    cout << out;
}