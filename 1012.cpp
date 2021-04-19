#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second


int board[52][52];
bool dist[52][52];
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	int tc;
	int x,y;
	cin >> t;
	while(t--) {
		cin >> n >> m >> tc;
		queue<pair<int,int>> Q;
		for(int i = 0; i < tc; i++) {
			cin >> x >> y;
			board[y][x] = 1;
		}
		
		int cnt = 0;
		for(int i = 0; i <= m-1; i++) {
			for(int j = 0; j <= n-1; j++) {
				if(board[i][j] == 0 || dist[i][j]) continue;
				cnt++;
				Q.push({i,j});
				dist[i][j] = 1;
				while(!Q.empty()) {
					auto cur = Q.front(); Q.pop();
					for(int dir = 0; dir < 4; dir++) {
						int xn = cur.X + dx[dir];
						int yn = cur.Y + dy[dir];
						if(xn < 0 || xn >= m || yn < 0 || yn >= n) continue;
						if(dist[xn][yn] || board[xn][yn] == 0) continue;
						dist[xn][yn] = 1;
						Q.push({xn,yn});
					}
				}
 			}
		}
		memset(board, 0, sizeof(board));
		memset(dist, 0, sizeof(dist));
		cout << cnt << endl;
	}	
}