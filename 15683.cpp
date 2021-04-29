#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[9][9];
int n,m;
int cctv_x,cctv_y;
int lit_x,lit_y;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<pair<int,int>> Q;
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> board[i][j];
            if(board[i][j] > 0 && board[i][j] <= 5) {
                cctv_x = i;
                cctv_y = j;
                Q.push({i,j});
            } else if (board[i][j] == 6) {
                lit_x = i;
                lit_y = j;
            }
        }
    }
    while(!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        if(board[cur.X][cur.Y] == 1) {
            int move = 0;
            int cnt = 0;
            int tmpx = cur.X;
            int tmpy = cur.Y;
            while(cnt < 4) {
                if(cnt == 0) {
                    if(tmpy <= m && board[tmpx][tmpy+1] != 6) {
                        board[tmpx][tmpy++]; // 오른쪽
                        move++;
                    } else {
                        tmpx = cur.X;
                        tmpy = cur.Y;
                        cnt++;
                        
                    }
                }else if (cnt == 1) {
                    board[tmpx++][tmpy]; // 아래
                } else if (cnt == 2) {
                    board[tmpx][tmpy--]; // 왼쪽
                } else if (cnt == 3) {
                    board[tmpx--][tmpy]; // 위
                }
            }
        }  
    }
    
}