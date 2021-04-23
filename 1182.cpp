#include <bits/stdc++.h>
using namespace std;

int n,s;
int board[30];
int cnt = 0;
void func(int k, int tmp) {
    if(k == n) {
        if(tmp == s)
            cnt++;
        return;
    }

    func(k+1, tmp);
    func(k+1, tmp+board[k]);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> s;
    for(int i = 0; i < n; i++) {
        cin >> board[i];
    }
    func(0,0);
    if(s==0) cnt--;
    cout << cnt << endl;
}