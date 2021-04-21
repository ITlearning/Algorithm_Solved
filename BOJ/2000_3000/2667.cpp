#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string board[1002];
bool dist[1002][1002];
int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};
int n,cnt;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    vector<int> v;
    
    for(int i = 0; i < n; i++) {
        cin >> board[i];
    }
    
    for(int i = 0; i < n; i++) fill(dist[i], dist[i]+n, false);

    int mx = 0;
    cnt = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(board[i][j] == '0' || dist[i][j]) continue;
            cnt++; 
            int num = 0;
            queue<pair<int,int>> Q;
            Q.push({i,j});
            dist[i][j] = 1;
           
            while(!Q.empty()) {
                num++;
                auto cur = Q.front(); Q.pop();
                for(int dir = 0; dir < 4; dir++) {
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if(dist[nx][ny] || board[nx][ny] == '0' ) continue;
                    dist[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
            v.push_back(num);
        }
    }

    sort(v.begin(), v.end());
    cout << cnt << '\n';
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << '\n';
    }
}