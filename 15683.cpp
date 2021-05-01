#include <bits/stdc++.h>
using namespace std;
#define X first;
#define Y second

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1}; // 인덱스 0,1,2,3이 남,동,북,서. 시계방향으로 돌아가는것.
int n,m;
int board1[10][10]; // 입력으로 주어지느 사무실의 모양을 저장할 변수
int board2[10][10]; // cctv의 방향을 정한 후에 cctv의 감시영역에 걸리는 빈칸은 값을 7로 바꾸는 작업을 수행 할 변수
vector<pair<int,int>> cctv;

bool OOB(int a, int b) {
    return a < 0 || a >= n || b < 0 || b >= m;
}

void upd(int x, int y, int dir) { 
    dir %= 4;
    while(1) {
        x += dx[dir];
        y += dy[dir];
        if(OOB(x,y)|| board2[x][y] == 6) return;
        if(board2[x][y] != 0) continue;
        board2[x][y] = 7; 
    }
}
// upd 설명
// (x,y) 에서 dir방향으로 진행하면서 벽을 만날 때 까지 지나치는 모든 빈 칸을 7로 바꾼다.



int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    int mn = 0; // 사각지대의 크기를 저장하는 변수. 0 개수 세는 것
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> board1[i][j];
            if(board1[i][j] != 0 && board1[i][j] != 6)
                cctv.push_back({i,j});
            if(board1[i][j] == 0) mn++;
        }
    }

    for(int tmp = 0; tmp < (1<<(2*cctv.size())); tmp++) {
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)// 4로 나눈 나머지를 뽑아 방향으로 사용하고
                board2[i][j] = board1[i][j];
        int brute = tmp;
        for(int i = 0; i < cctv.size(); i++) {
            int dir = brute % 4;  
            brute /=4;
            int x = cctv[i].X;
            int y = cctv[i].Y;
            if(board1[x][y] == 1) {
                upd(x,y,dir);
            } else if (board1[x][y] == 2) {
                upd(x,y,dir);
                upd(x,y,dir+2);
            } else if (board1[x][y] == 3) {
                upd(x,y,dir);
                upd(x,y,dir+1);
            } else if (board1[x][y] == 4) {
                upd(x,y,dir);
                upd(x,y,dir+1);
                upd(x,y,dir+2);
            } else {
                upd(x,y,dir);
                upd(x,y,dir+1);
                upd(x,y,dir+2);
                upd(x,y,dir+3);
            } 
        }
        int val = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                val += (board2[i][j]==0);
        mn = min(mn,val);
    }
    cout << mn;
}