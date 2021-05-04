#include <bits/stdc++.h>
using namespace std;
int board[8] = {};
int tmp[8] = {0,2,0,2,8,8,0,16};
void left() {
    bool x[8] = {};
    int idx = 0;
    for(int i = 0; i < 8; i++) {
        if(tmp[i] != 0) {
            if(board[idx] == tmp[i] && x[idx] != true) {
                board[idx] *= 2;
                x[idx] = true;
            }
            board[idx] = tmp[i];
        }
    }
}

int main() {
    for(int i = 0; i < 3; i++) {
        cout << board[i] << endl;

    }
}