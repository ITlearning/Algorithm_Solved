#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
int n,m;
int board[10];
int isused[10];
/*
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
            board[k] = i;
            func(i+1, k+1);
            isused[i] = 0;
        }
    }
}
*/

//next_premutation
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    //func(1, 0);
    for(int i = 0; i < n; i++) {
        if(i < m) board[i] = 0;
        else board[i] = 1;
    }

    do{
        for(int i = 0; i < n; i++) {
            if(board[i] == 0) cout << i + 1 << ' ';
        }
        cout << '\n';
    } while(next_permutation(board,board+n));
}