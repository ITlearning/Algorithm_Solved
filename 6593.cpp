#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
char board[50][50][50];
int dist[50][50][50];
int dx[6] = {-1,1,0,0,0,0};
int dy[6] = {0,0,-1,1,0,0};
int dz[6] = {0,0,0,0,-1,1};
int l,r,c;
int tmpz;
int tmpy;
int tmpx;
int anx;
int anh;
int anz;
struct ThreeBox {
	int x,y,z;
};


void bfs() {
		queue<ThreeBox> Q;
		Q.push({tmpx,tmpy,tmpz});
		while(!Q.empty()) {
		int x = Q.front().x;
		int y = Q.front().y;
		int z = Q.front().z;
		Q.pop();
		
		if(x == anx && y == anh && z == anz) {
			cout << "Escaped in " << dist[x][y][z] << "minute(s)." << endl;
			return;
		}
		
	
		for(int i = 0; i < 6; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			int nz = z + dz[i];
			if(nx < 0 || nx >= l || ny < 0 || ny >= r || nz < 0 || nz >= c) continue;
			if(dist[nx][ny][nz] || board[nx][ny][nz] == '#') continue;
			Q.push({nx,ny,nz});
			dist[nx][ny][nz] = dist[x][y][z]+1;
			}
		}
	cout << "Teapped!" << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	while(true) {
		memset(dist, false, sizeof(dist));
		cin >> l >> r >> c;
		if(l == 0 && r == 0 && c == 0) {
			return 0;
		}
		
		
		for(int i = 0; i < l; i++) {
			for(int j = 0; j < r; j++) {
				for(int k = 0; k < c; k++) {
					cin >> board[i][j][k];
					if(board[i][j][k] == 'S') {
						tmpx = i; tmpy = j; tmpz = k;
					}else if(board[i][j][k] == 'E') {
						anx = i;anh = j;anz = k;
					}
				}
			}
		}
		bfs();
		//Q.clear();
	}
}