#include <bits/stdc++.h>
using namespace std;

int board[64][64];

void func(int n,int x,int y) {
    int one = 0;
    int zero = 0;
    if(x == 1) {
        cout << board[x][y];
        return;
    }

    for(int i = x; i < x+n; i++) {
        for(int j = y; j < y+n; j++) {
            if(board[i][j] == 1) {
                one++;
            } else {
                zero++;
            }
        }
    }

    if(one == n*n) {
        cout << 1;
    } else if (zero == n*n) {
        cout << 0;
    }
    else {
        cout << "(";
        func(n/2,x,y);
        func(n/2, x, y+n/2);
        func(n/2,x+n/2,y);
        func(n/2, x+n/2, y+n/2);
        cout << ")";
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    string s;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;
        for(int j = 0; j < n; j++) {
           board[i][j] = s[j] - '0';
        }
    }
    func(n,0,0);
}