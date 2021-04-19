#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[502][502];
bool dist[502][502];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int n,m;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;

	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			cin >> board[i][j];
		}
	}
	
	int mx = 0;
	int cnt = 0;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(board[i][j] == 0 || dist[i][j])	continue;
			cnt++;
			int num = 0;
			queue<pair<int,int>> Q;
			Q.push({i,j});
			dist[i][j] = 1;
			while(!Q.empty()) {
				num++;
				auto cur = Q.front(); Q.pop();
				for(int dir = 0; dir < 4; dir++) {
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
					if(dist[nx][ny] || board[nx][ny] == 0) continue;
					dist[nx][ny] = 1;
					Q.push({nx,ny});
					
				}
			}
			mx = max(mx, num);
		}
	}
	cout << cnt << '\n' <<  mx;
}