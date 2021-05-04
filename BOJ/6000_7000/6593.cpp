#include <bits/stdc++.h>
using namespace std;

char board[31][31][31];
int dist[31][31][31];
int dx[6] = {0,0,1,-1,0,0};
int dy[6] = {1,-1,0,0,0,0};
int dz[6] = {0,0,0,0,1,-1};
int l,r,c;
int tmpz;
int tmpy;
int tmpx;


int main() {
	//ios::sync_with_stdio(0);
	cin.tie(0);
	
	while(true) {
		int cnt = 0;
		cin >> l >> r >> c;
		if(l == 0 && r == 0 && c == 0) {
			return 0;
		}
		queue<pair<pair<int,int>,int>> Q;
		for(int i = 0; i < l; i++) {
			for(int j = 0; j < r; j++) {
				for(int k = 0; k < c; k++) {
					cin >> board[i][j][k];
					if(board[i][j][k] == 'S') {
						Q.push({{i,j},k});
					} else if (board[i][j][k] == 'E') {
						tmpz = i; tmpy = j; tmpx = k;
					}
				}
			}
		}
			
		bool t = true;
		while(!Q.empty()) {
		int z = Q.front().first.first;
		int y = Q.front().first.second;
		int x = Q.front().second;
		Q.pop();
		
		for(int i = 0; i < 6; i++) {
			int nz = z + dz[i];
			int ny = y + dy[i];
			int nx = x + dx[i];
			if(nx < 0 || nx >= c || ny < 0 || ny >= r || nz < 0 || nz >= l) continue;
			if(board[nz][ny][nx] == '#' || dist[nz][ny][nx] != 0) continue;
			if(board[nz][ny][nx] == 'E') {
				t = false;
				}
			Q.push({{nz,ny},nx});
			dist[nz][ny][nx] = dist[z][y][x]+1;
			}
		}
		if(t) {
			cout << "Trapped!" << endl;
		} else {
			cout << "Escaped in " << dist[tmpz][tmpy][tmpx] << " minute(s)." << endl;
		}
		
		for (int i = 0; i < l; i++) {
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++) {
				
					dist[i][j][k] = false;
				}
			}
		}
	}
}