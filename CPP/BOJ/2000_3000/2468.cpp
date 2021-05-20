#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int n,m;
int board[101][101];
int rain[101][101];
bool dist[101][101];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int total, max_val;
int result;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n;
	int cnt = 0;
	queue<pair<int,int>> Q;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			cin >> board[i][j];
			max_val = max(max_val, board[i][j]);
		}
	}
	
	for(int i = 0; i <= max_val; i++) {
		for(int j = 0; j < n; j++) {
			for(int k = 0; k < n; k++) {
				if(board[j][k] <= i) {
					rain[j][k] = 1; // 잠긴거면 1 아니면 0
				}
			}
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(rain[i][j] == 0 && dist[i][j] == 0) {
					cnt++;
					dist[i][j] = 1;
					Q.push({i,j});
					while(!Q.empty()) {
						auto cur = Q.front(); Q.pop();
						for(int dir = 0; dir < 4; dir++) {
							int nx = cur.X + dx[dir];
							int ny = cur.Y + dy[dir];
							if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
							if(dist[nx][ny] || rain[nx][ny]) continue;
							dist[nx][ny] = 1;
							Q.push({nx,ny});
						}
					}
				}
			}
		}
		total = max(total,cnt);
		cnt = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				dist[i][j] = 0;
				rain[i][j] = 0;
			}
		}
	}
	cout << total << '\n';
}