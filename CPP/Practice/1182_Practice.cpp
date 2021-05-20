#include <bits/stdc++.h>
using namespace std;

int n,s;
int board[30];
int cnt = 0;
void func(int a,int tmp) {
    if(a == n) {
        if(tmp == s) {
            cnt++;
        }
        return;
    } 

    func(a+1, tmp);
    func(a+1, tmp+board[a]);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> s;
    for(int i = 0; i < n; i++) {
        cin >> board[i];
    }
    func(0,0);
    cout << cnt << endl;
}