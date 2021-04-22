#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define endl '\n'
int board[100][100];
bool dist[100][100];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};
int m,n,k;
int box = 0;
vector<int> v;
queue<pair<int,int>> Q;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    memset(dist,false,sizeof(dist));
    memset(board,0,sizeof(board));
    int x1,y1,x2,y2;
    cin >> m >> n >> k;
    for(int i = 0; i < k; i++) {
        cin >> x1 >> y1 >> x2 >> y2;

        for(int j = x1; j < x2; j++) {
            for(int p = y1; p < y2; p++) {
                board[p][j] = 1;
            }
        }
    }
    
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            cout << board[i][j] << ' ';
        }
        cout << endl;
    }
    cout << endl;
    for(int i = 0; i < m; i++) {
        int cnt = 0;
        for(int j = 0; j < n; j++) {
            if(board[i][j] == 1) continue;
            
            Q.push({i,j});
            dist[i][j] = true;
            while(!Q.empty()) {
            auto cur = Q.front(); Q.pop();
            for(int dir = 0; dir < 4; dir++) {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if(board[nx][ny] == 1 || dist[nx][ny] == true) continue;
                cnt++;
                dist[nx][ny] = true;
                Q.push({nx,ny});
                }
            }
            
        }
        v.push_back(cnt);
    } 
    cout << box << endl;
    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << ' ';
    }
}