#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string board[102];
bool dist[102][102];
int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};
int n,cnt;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    
    for(int i = 0; i < n; i++) {
        cin >> board[i];
    }
    
    memset(dist, false, sizeof(dist));
    int gcnt = 0;
    int rcnt = 0;
    int bcnt = 0;
    int dcnt = 0;
    cnt = 0;
    // B 영역
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if( dist[i][j] || board[i][j] == 'R' || board[i][j] == 'G') continue;
            bcnt++; 
            queue<pair<int,int>> Q;
            Q.push({i,j});
            dist[i][j] = 1;
            while(!Q.empty()) {
                auto cur = Q.front(); Q.pop();
                for(int dir = 0; dir < 4; dir++) {
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if( dist[nx][ny] || board[nx][ny] == 'R' || board[nx][ny] == 'G') continue;
                    dist[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }
    // R 영역
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(dist[i][j] || board[i][j] == 'B' || board[i][j] == 'G') continue;
            rcnt++; 
            queue<pair<int,int>> Q;
            Q.push({i,j});
            dist[i][j] = 1;
            while(!Q.empty()) {
                auto cur = Q.front(); Q.pop();
                for(int dir = 0; dir < 4; dir++) {
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if(dist[nx][ny] || board[nx][ny] == 'B' || board[nx][ny] == 'G') continue;
                    dist[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }
    // g영역
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if( dist[i][j] || board[i][j] == 'R' || board[i][j] == 'B') continue;
            gcnt++; 
            queue<pair<int,int>> Q;
            Q.push({i,j});
            dist[i][j] = 1;
            while(!Q.empty()) {
                auto cur = Q.front(); Q.pop();
                for(int dir = 0; dir < 4; dir++) {
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if(dist[nx][ny] || board[nx][ny] == 'R' || board[nx][ny] == 'B') continue;
                    dist[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }
    // R과 G를 합친걸 세는 것
    memset(dist, false, sizeof(dist));
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if( dist[i][j] || board[i][j] == 'B') continue;
            dcnt++; 
            queue<pair<int,int>> Q;
            Q.push({i,j});
            dist[i][j] = 1;
            while(!Q.empty()) {
                auto cur = Q.front(); Q.pop();
                for(int dir = 0; dir < 4; dir++) {
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if(dist[nx][ny] || board[nx][ny] == 'B') continue;
                    dist[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }
    cnt = rcnt + gcnt + bcnt;
    cout << cnt << ' ';
    cout << bcnt + dcnt;
    
}