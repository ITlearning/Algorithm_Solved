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
int any;
int anz;
struct ThreeBox {
	int x,y,z;
};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	while(true) {
		memset(dist, false, sizeof(dist));
		string str;
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
						dist[i][j][k] == 1;
					}else if(board[i][j][k] == 'E') {
						anx = i;
						any = j;
						anz = k;
					}
				}
			}
		}
		queue<ThreeBox> Q;
		Q.push({tmpx,tmpy,tmpz});
		bool t = true;
		while(!Q.empty()) {
		int x = Q.front().x;
		int y = Q.front().y;
		int z = Q.front().z;
		Q.pop();
		for(int i = 0; i < 6; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			int nz = z + dz[i];
			if(nx < 0 || nx >= l || ny < 0 || ny >= r || nz < 0 || nz >= c) continue;
			if(board[nz][ny][nx] == '#' || dist[nz][ny][nx] > 0) continue;
			if(x == anx && y == any && z == anz) {
				cout << "Escaped in " << dist[x][y][z] << "minute(s)." << endl;
				t = false;
				continue;
			}
			Q.push({nx,ny,nz});
			dist[nx][ny][nz] = dist[x][y][z]+1;
			}
		}
		if(t) {
			cout << "Teapped!" << endl;
		}
		//Q.clear();
	}
	
}