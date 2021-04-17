#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
<<<<<<< HEAD
int board[502][502];
bool vis[502][502];
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1}; // 상하좌우 네 방향을 의미

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
	
  cin >> n >> m;
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++)
      cin >> board[i][j];
  int mx = 0; // 그림의 최댓값
  int num = 0; // 그림의 수

  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){ 
      if(board[i][j] == 0 or vis[i][j]) continue; 
      num++; 
      queue<pair<int,int> > Q;
      vis[i][j] = 1; 
      Q.push({i,j});
      int area = 0;
      while(!Q.empty()){
        area++;
        auto cur = Q.front(); Q.pop();
        for(int dir = 0; dir < 4; dir++){
          int nx = cur.X + dx[dir];
          int ny = cur.Y + dy[dir];
          if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
          if(vis[nx][ny] || board[nx][ny] != 1) continue;
          vis[nx][ny] = 1;
          Q.push({nx,ny});
        }
      }
      mx = max(mx, area);
=======
int board[1002][1002];
int dist[1002][1002];
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> m >> n;
  queue<pair<int,int> > Q;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cin >> board[i][j];
      if(board[i][j] == 1)
        Q.push({i,j});
      if(board[i][j] == 0)
        dist[i][j] = -1;
    }
  }
  while(!Q.empty()){
    auto cur = Q.front(); Q.pop();
    for(int dir = 0; dir < 4; dir++){
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
      if(dist[nx][ny] >= 0) continue;
      dist[nx][ny] = dist[cur.X][cur.Y]+1;
      Q.push({nx,ny});
    }
  }
  int ans = 0;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      if(dist[i][j] == -1){
        cout << -1;
        return 0;
      }
      ans = max(ans, dist[i][j]);
>>>>>>> fe30384ebe75e7e2e5f8bdef1c1b1ccd24522909
    }
  }
  cout << ans;
}