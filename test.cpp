#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
int board[101][101];
int check[101][101];
int rain[101][101];

int main() {
	ios::sync_with_stdio(NULL);
	cin.tie(NULL);
	int N;
	int heightMax = 0, caseMax = 0;
	int num = 0;
	queue<pair<int, int>> Q;
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
			heightMax = max(heightMax, board[i][j]);
		}

	for (int i = 0; i <= heightMax; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (board[j][k] <= i) {
					rain[j][k] = 1; //비에 잠긴 곳이 1 비에 안 잠긴 곳이 0 안 잠긴 곳으로 BFS
				}
			}
		}
		for (int p = 0; p < N; p++) {
			for (int q = 0; q < N; q++) {
				if (rain[p][q] == 0 && check[p][q] == 0) {
					num++;
					check[p][q] = 1;
					Q.push({ p,q });
					while (!Q.empty()) {
						auto cur = Q.front();
						Q.pop();
						for (int idx = 0; idx < 4; idx++) {
							int nx = cur.first + dx[idx];
							int ny = cur.second + dy[idx];
							if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
							if (check[nx][ny] == 1 || rain[nx][ny] == 1) continue;
							check[nx][ny] = 1;
							Q.push({ nx,ny });
						}
					}
				}
			}
		}
		caseMax = max(caseMax, num);
		num = 0;
		for (int p = 0; p < N; p++)
			for (int q = 0; q < N; q++) {
				rain[p][q] = 0;
				check[p][q] = 0;
			}
	}
	cout << caseMax;
}