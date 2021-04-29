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
int cX[9];
int cY[9];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<pair<pair<int, int>,int>> Q;
    cin >> n >> m;
    int location = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
            if (board[i][j] > 0 && board[i][j] <= 5)
            {
                cX[location] = i;
                cY[location] = j;
                location++;
                Q.push({{i, j},board[i][j]});
            }
            else if (board[i][j] == 6)
            {
                lit_x = i;
                lit_y = j;
            }
        }
    }
    int Gak_move[4] = {};
    int box_size = 0;
    int total_small = 0;
    while(!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        int x = cur.X.X;
        int y = cur.X.Y;
        int cN = cur.Y;
        int cnt = 0;
        int move = 0;
        int small = 0;
        if(cN == 1) {
            while(cnt < 4) {
                if(cnt == 0) {
                    if(y <= m && board[x][y+1] != 6) {
                        y++;
                        move++;
                    } else {
                        x = cur.X.X;
                        y = cur.X.Y;
                        Gak_move[0] = move;
                        move = 0;
                        cnt++;
                    }
                } else if(cnt == 1) {
                    if(x <= n && board[x+1][y] != 6) {
                        x++;
                        move++;
                    } else {
                        x = cur.X.X;
                        y = cur.X.Y;
                        Gak_move[1] = move;
                        move = 0;
                        cnt++;
                    }
                } else if(cnt == 2) {
                    if(y > 0 && board[x][y-1] != 6) {
                        y--;
                        move++;
                    } else {
                        x = cur.X.X;
                        y = cur.X.Y;
                        Gak_move[2] = move;
                        move = 0;
                        cnt++;
                    }
                } else if(cnt == 3) {
                    if(x > 0 && board[x-1][y] != 6) {
                        x--;
                        move++;
                    } else {
                        x = cur.X.X;
                        y = cur.X.Y;
                        Gak_move[3] = move;
                        move = 0;
                        cnt++;
                    }
                }
            }

            for (int i = 0; i < 4; i++)
                {
                    if (Gak_move[i] <= Gak_move[i + 1])
                    {
                        small = i;
                    }
                    else
                    {
                        small = i + 1;
                    }
                }
                
            if(small == 0) {
                    for(int i = y; i < m ;i++) {
                        if(board[x][i] != 6) {
                            board[x][i] = '#';
                        } else {
                            break;
                        }
                    }
                } else if(small == 1) {
                    for(int i = x; i < n; i++) {
                        if(board[i][y] != 6) {
                            board[i][y] = '#';
                        } else {
                            break;
                        }
                    }
                } else if(small == 2) {
                    for(int i = y; i >= 0; i--) {
                        if(board[x][i] != 6) {
                            board[x][i] = '#';
                        } else {
                            break;
                        }
                    }
                } else if(small == 3) {
                    for(int i = x; i >= 0; i--) {
                        if(board[i][y] != 6) {
                            board[i][y] = '#';
                        } else {
                            break;
                        }
                    }
                }
        } else if(cN == 2) {

        } else if(cN == 3) {

        } else if(cN == 4) {

        } else if(cN == 5) {

        }

    }
    
    for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (board[i][j] == 0)
                    {
                        box_size++;
                    }
                }
            }
    cout << box_size << endl;
}
