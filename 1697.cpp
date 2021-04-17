#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int dist[100002];
int n, m;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	fill(dist, dist+100001, -1);
	queue<int> Q;
	Q.push(n);
	dist[n] = 0;
	while(dist[m] == -1) {
		auto cur = Q.front(); Q.pop();
		for(int nxt : {cur-1, cur+1, cur*2}) {
			if(nxt < 0 || nxt > 100000) continue;
			if(dist[nxt] != -1) continue;
			dist[nxt] = dist[cur]+1;
			Q.push(nxt);
		}
	}
	cout << dist[m];
}