#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board1[10][10]; // 원래 보드 작성 칸
int board2[10][10]; // 사각 지대의 개수를 세기 위한 보드
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
vector<pair<int,int>> cctv;

bool OOP(int a,int b) {
    return a < 0 || a >= n || b < 0 || b >= m;
}


// (x,y)에서 dir 방향으로 진행하며 벽을 만나기 전까지 지나가는 모든 칸을 7로 바꿈
void func(int x, int y, int dir) {
    dir %= 4;
    while(1) {
        x += dx[dir];
        y += dy[dir];
        if(OOP(x,y) || board2[x][y] == 6) return;
        if(board2[x][y] != 0) continue;
        board2[x][y] = 7;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int mn = 0; // 사각 지대의 최소 크기 답
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> board1[i][j];
            if(board1[i][j] != 0 && board1[i][j] != 6) {
                cctv.push_back({i,j});
            }
            if(board1[i][j] == 0) mn++; // 일단 원래의 사각지대 개수(0의 초기 개수)를 세는 것.
        }
    }

    // 1 << (2*cctv.size())는 4의 cctv.size()승을 의미.
    for(int tmp = 0; tmp < (1<<(2*cctv.size())); tmp++) {
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                board2[i][j] = board1[i][j]; // 사각지대 보드에 복사
        int brute = tmp; // 임시 변수에 옮겨서 사용해야 tmp의 원래 값이 변경되지 않을 것이기 때문에 옮기는 것 같다.
        for(int i = 0; i < cctv.size(); i++) {
            int dir = brute % 4;
            brute /= 4;
            int x = cctv[i].X;
            int y = cctv[i].Y;
            if(board1[x][y] == 1) {
                func(x,y,dir); // 한번에 한 방향만 이동 가능하니, 당연히 이렇게 사용한다.
            } else if (board1[x][y] == 2) {
                func(x,y,dir); // dir이 0 일때
                func(x,y,dir+2); // dir이 0 +2 이기에 (0,2) 뭐 이렇게 시작하니까 위,아래 왼쪽, 오른쪽 동시에 보기가 가능하다.
            } else if (board1[x][y] == 3) {
                func(x,y,dir); // 3의 경우 한번에 두개의 방향 ,예를 들면 위 오른쪽 뭐 이렇게 돌아가니까 하나 다음 인덱스의 숫자를 호출
                func(x,y,dir+1);
            } else if(board1[x][y] == 4) {
                func(x,y,dir);
                func(x,y,dir+1);
                func(x,y,dir+2);
            } else {
                func(x,y,dir);
                func(x,y,dir+1);
                func(x,y,dir+2);
                func(x,y,dir+3);
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