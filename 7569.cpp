#include <bits/stdc++.h>
using namespace std;

int board[102][102][102];
bool dist[102][102][102];
int dx[6] = {1,-1,0,0,0,0};
int dy[6] = {0,0,1,-1,0,0};
int dh[6] = {0,0,0,0,1,-1};
int n,m,h;

int main() {
	ios::sync_with_stdio(0);
	
	cin >> m >> n >> h;
	queue<tuple<int,int,int>> Q;
	
	for(int z = 0; z < h; z++) {
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				cin >> board[i][j][z];
				if(board[i][j][z] == 1) {
					Q.push(make_tuple(i, j, z));
				}
				if(board[i][j][z] == 0) {
					dist[i][j][z] = true;
				}
			}
		}
	}
	
	if(Q.empty()) {
		cout << -1;
		return 0;
	}
	
	
	int cnt = 0;
	while(!Q.empty()) {
		int x,y,z = 0;
		tie(x,y,z) = Q.front(); Q.pop();
		dist[x][y][z] = true;
		for(int dir = 0; dir < 6; dir++) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			int nz = z + dh[dir];	
			if(nx >= 0 && ny >= 0 && nz >= 0 && nx < n && ny < m && nz < h && !dist[nx][ny][nz]) {
				dist[nx][ny][nz] = true;
				cnt++;
				Q.push(make_tuple(nx, ny, nz));
			}
			
		}
	}
	
	for(int i = 0; i < h; i++) {
		for(int j = 0; i < n; j++) {
			for(int k = 0; k < m; k++) {
				if(dist[j][k][i] == -1) {
					cout << -1;
					return 0;
				}
			}
		}
	} 
	cout << cnt << endl;
	
}