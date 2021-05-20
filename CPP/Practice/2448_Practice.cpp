#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

const int MAX = 10000;
bool board[MAX][MAX];

void star(int n, int x, int y) {
    if(n==3) {
        board[x][y] = true;
        board[x+1][y-1] = true;
        board[x+1][y+1] = true;
        for(int i = 0; i < 5; i++) {
            board[x+2][y-i+2] = true;
        }
        return;
    }

    star(n/2, x,y);
    star(n/2, x+n/2,y-n/2);
    star(n/2, x+n/2,y+n/2);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int input;
    cin >> input;
    star(input, 0, input-1);
    for(int i = 0; i < input; i++) {
        for(int j = 0; j < 2*input - 1; j++) {
            if(board[i][j]) cout << "*";
            else cout << " ";
        }
        cout << endl;
    }
}