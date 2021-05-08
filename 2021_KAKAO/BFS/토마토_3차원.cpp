#include <bits/stdc++.h>
using namespace std;

int board[102][102][102];
int dist[102][102][102];
int dx[6] = {0,0,1,-1,0,0};
int dy[6] = {1,-1,0,0,0,0};
int dz[6] = {0,0,0,0,1,-1};
int n,m,h;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> m >> n >> h;
	queue<pair<pair<int,int>,int>> Q;
	
	for(int k = 0; k < h; k++) {
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				cin >> board[i][j][k];
				dist[i][j][k] = -1;
				if(board[i][j][k] == 1) {
					Q.push(make_pair(make_pair(i,j),k));
					dist[i][j][k] = 0;
				}
			}
		}
	}
	
	
	while(!Q.empty()) {
		int x = Q.front().first.first;
		int y = Q.front().first.second;
		int z = Q.front().second;
		Q.pop();
		
		for(int i = 0; i < 6; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			int nz = z+dz[i];
			
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if(nz < 0 || nz >= h) continue;
			
			if(board[nx][ny][nz] == 0 && dist[nx][ny][nz] == -1) {
				Q.push(make_pair(make_pair(nx,ny),nz));
				dist[nx][ny][nz] = dist[x][y][z]+1;
			}
		}
	}
	
	int ans = 0;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			for(int k = 0; k < h; k++) {
				if(board[i][j][k] ==0 && dist[i][j][k] == -1) {
					ans = -1;
					break;
				}
				if(ans < dist[i][j][k])
                    ans = dist[i][j][k];
            }
            if(ans == -1) break;
            
        }
        if(ans == -1) break;
	}
	
	cout << ans;
}