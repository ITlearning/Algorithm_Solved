#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[10002][1002];
int dist[1002][1002];
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> m >> n;
	queue<pair<int,int>> Q;
	// 먼저 입력할때 익은것이 어디에 있는지를 큐에 적어놓으면 그거 따라서 퍼뜨리면 되는 것.
	// 하나 이상이니까 하나만 있는 경우도 있지만 다수일때도 존재하기 때문.
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			cin >> board[i][j];
			if(board[i][j] == 1) {
				Q.push({i,j});
			}
			if(board[i][j] == 0) {
				dist[i][j] = -1;
			}
		}
	}
	
	while(!Q.empty()) {
		auto cur = Q.front(); Q.pop();
		for(int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if(dist[nx][ny] >= 0) continue;
			dist[nx][ny] = dist[cur.X][cur.Y]+1;
			Q.push({nx,ny});
		}
	}
	
	int ans = 0;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(dist[i][j] == -1) {
				cout << -1;
				return 0;
			}
			ans = max(ans, dist[i][j]);
		}
	}
	cout << ans;
}