#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

string board[1002];
int dist[1002][1002];
int pdist[1002][1002];
int r, c;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> r >> c;
	for(int i = 0; i < r; i++) {
		cin >> board[i];
	}
	queue<pair<int,int>> Q1;
	queue<pair<int,int>> Q2;
	for(int i = 0; i < r; i++){
		fill(dist[i], dist[i]+c, -1);
		fill(pdist[i],pdist[i]+c, -1);
	} 
	
	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			if(board[i][j] == 'F') {
				Q1.push({i,j});
				dist[i][j] = 0;
			}
			if(board[i][j] == 'J') {
				Q2.push({i,j});
				pdist[i][j] = 0;
			}
		}
	}
	// ∫“ BFS
	while(!Q1.empty()) {
		auto cur = Q1.front(); Q1.pop();
		for(int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if(nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
			if(dist[nx][ny] >= 0 || board[nx][ny] == '#') continue;
			dist[nx][ny] = dist[cur.X][cur.Y]+1;
			Q1.push({nx,ny});
		}
	}
	
	// ¡ˆ»∆¿Ã BFS
	while(!Q2.empty()) {
		auto cur = Q2.front(); Q2.pop();
		for(int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if(nx < 0 || nx >= r || ny < 0 || ny >= c) {
				cout << pdist[cur.X][cur.Y]+1;
				return 0;
			}
			if(pdist[nx][ny] >= 0 || board[nx][ny] == '#') continue;
			if(dist[nx][ny] != -1 && dist[nx][ny] <= pdist[cur.X][cur.Y]+1) continue; //Î∂àÏù¥ Í∞ôÏù¥ ?ûàÍ±∞ÎÇò ?çî Îπ®Î¶¨ ?êúÍ±∞Î©¥ Ïß??ÇòÍ∞àÏàò ?óÜÍ∏? ?ïåÎ¨∏Ïóê ?ù¥?ü∞ Ï°∞Í±¥Î¨∏ÏùÑ ?ÇΩ?ûÖ.
			pdist[nx][ny] = pdist[cur.X][cur.Y]+1;
			Q2.push({nx,ny});
		}
	}
	cout << "IMPOSSIBLE";
}