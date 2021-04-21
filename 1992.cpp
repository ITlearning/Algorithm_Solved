#include <bits/stdc++.h>
using namespace std;

int board[64][64];

void func(int n, int x, int y) {
    int a_true = 0;
    int a_false = 0;
    if(n==1) {
        cout << board[x][y];
        return;
    }
    for(int i = x; i < x+n; i++) {
        for(int j = y; j < y+n; j++) {
            if(board[i][j] == 1) {
                a_true++;
            } else {
                a_false++;
            }
        }
    }

    if(a_true == n*n) { // 모든 수가 1일경우
        cout << 1;
    }else if(a_false == n*n){ // 모든 수가 0일 경우
        cout << 0;
    }
    else {
        cout << "(";
        func(n/2,x,y);
        func(n/2,x,y+n/2);
        func(n/2,x+n/2,y);
        func(n/2,x+n/2,y+n/2);
        cout << ")";
    }
}

int main() {
    int n;
    string s;
    cin >> n;
    for(int i = 0; i < n;i++) {
        cin >> s;
        for(int j = 0; j < n;j++) {
            board[i][j] = s[j]-'0';
        }
    }
    func(n,0,0);
    return 0;
}
