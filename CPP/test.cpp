#include <bits/stdc++.h>
using namespace std;
#include X first
#include Y second

int board[102][102];
bool dist[102][102];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};
int n,m,k;
int x1,x2,y1,y2;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	vector<int> v;
	queue<pair<int,int> > Q;

	cin >> m >> n >> k;
	for(int i = 0; i < k; i++) {
		cin >> x1 >> y1 >> x2 >>y2;

		for(int j = x1; j < x2; j++) {
			for(int k = y1; k < y2; k++) {
				board[k][j] = 1;
			}
		}
	}
	int cnt = 0;
	for(int i = 0; i < m; i++) {
		for(int j = 0; j < n; j++) {
			if(board[i][j] == 1 || dist[i][j]) continue;
			cnt++;
			int box = 0;
			Q.push({i,j});
			dist[i][j] = 1;
			while(!Q.empty()) {
				box++;
				auto cur = Q.front(); Q.pop();
				for(int dir = 0; dir < 4; dir++) {
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if(nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
					if(dist[nx][ny] || board[nx][ny] == 1) continue;
					dist[nx][ny] = 1;
					Q.push({nx,ny});
				}
				v.push_back(box);
			}
		}
	}

	sort(v.begin(), v.end());
	cout << cnt;
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << ' ';
	}
}