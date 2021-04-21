#include <bits/stdc++.h>
using namespace std;

int board[100001];
bool vis[100001];
bool done[100001];
int t,n,cnt;

// dfs 공부하자.
void dfs(int n) {
	vis[n] = true;
	int next = board[n];
	if(!vis[next]) {
		dfs(next);
	}
	else if(!done[next]) {
		for(int i = next; i != n; i = board[i]) {
			cnt++;
		}
		cnt++;
	}
	done[n] = true;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> t;
	while(t--) {
		cnt = 0;
		fill(done,done+100001, false);
		fill(vis, vis+100001, false);
		cin >> n;
		for(int i = 0; i < n; i++) {
			cin >> board[i + 1];
		}
		for(int i =1; i <= n; i++) {
			if(!vis[i]) {
				dfs(i);
			}
		}
		cout << n - cnt << '\n';
	}
}