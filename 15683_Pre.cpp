#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[9][9];
int n, m;
int cctv_x, cctv_y;
int lit_x, lit_y;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int d1[4] = {-1,1,0,0};
int d2[4] = {0,0,-1,1};
int ld[4];
int ad[2];
int cY[9];
int zero = 0;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<pair<pair<int, int>,int>> Q;
    cin >> n >> m;
    int location = 0;
    // 이중 for문을 돌며 NxM크기의 직사각형을 만든다.
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> board[i][j];
            if(board[i][j] >= 1 && board[i][j] < 6) { // 이때 1 이상 6이하의 수가 등장했을 경우
                Q.push({{i,j}, board[i][j]});           // 큐에 위치와 숫자를 push한다.
            }
        }
    }

    while(!Q.empty()) {
        auto cur = Q.front();
        if(cur.Y == 1) { 
            for(int i = 0; i < 4; i++) {
                int tx = cur.X.X;
                int ty = cur.X.Y;
                int cnt = 0;
                while(tx >= 0 && tx <= n-1 && ty >= 0 && ty <= m-1) {
                    tx += dx[i];
                    ty += dy[i];
                    cnt++;
                    if(board[tx][ty] == 6) {
                        break;
                    }
                }
                cnt -= 1;
                ld[i] = cnt;
            }
            int k = 0;
            for(int i = 1; i < 3; i++) {
                if(ld[k] < ld[i]) {
                    k = i;
                }
            }
            int ax = cur.X.X;
            int ay = cur.X.Y;
            while(ax >= 0 && ax <= n && ay >= 0 && ay <= m) {
                ax += dx[k];
                ay += dy[k];
                if(board[ax][ay] != 6 || board[ax][ay] == 0) {
                    board[ax][ay] = 9;
                } else if (board[ax][ay] <= 5) {
                    continue;
                }
            }
            Q.pop();
        } else if(cur.Y == 2) {
            
        } else if(cur.Y == 3) {

        } else if(cur.Y == 4) {

        } else if(cur.Y == 5) {

        }
        
    }

    for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                cout << board[i][j] << ' ';
                    if(board[i][j] == 0) {
                        zero++;
                }
            }
            cout << endl;
        }

    cout << zero << endl;
}