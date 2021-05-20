#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[300][300];
bool dist[300][300];
int dy[8] = {2,1,-2,-1,-1,-2,1,2};
int dx[8] = {-1,-2,1,2,-2,-1,2,1};
int t,n;
int night_x, night_y, target_x, target_y;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	while(t--) {
		cin >> n;
		memset(board,0,sizeof(board));
		memset(dist, false, sizeof(dist));
		cin >> night_y >> night_x;
		cin >> target_y >> target_x;
		
		queue<pair<pair<int,int>,int>> Q;
		Q.push({{night_y,night_x},0});
		dist[night_y][night_x] = true;
		
		while(!Q.empty()) {
			auto cur = Q.front();
			
			if(cur.X.X == target_y && cur.X.Y == target_x) {
				cout << Q.front().Y << '\n';
				break;
			}
			
			for(int dir = 0; dir < 8; ++dir) {
				int nx = cur.X.Y + dx[dir];
				int ny = cur.X.X + dy[dir];
				int num = cur.Y;
				if(nx >= 0 && nx < n && ny >= 0 && ny < n) {
					if(dist[ny][nx] == false) {
						dist[ny][nx] = true;
						Q.push({{ny,nx}, num+1});
						
					}
				}
			}
			Q.pop();
		}
		
	}
}