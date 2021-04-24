#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n,m;
int board[10];
int isused[10];

void func(int num, int k) {
    if(k == m) {
        for(int i = 0; i < m; i++) {
            cout << board[i] << ' ';
        }
        cout << endl;
        return;
    }

    for(int i = num; i <= n; i++) {
        if(!isused[i]) {
            isused[i] = 1;
            board[k] = 1;
            func(i+1, k+1);
            isused[i] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    func(1,0);
   vector<int> v;
}
