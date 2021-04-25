#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n,m;
int board[10];
int isused[10];

void func(int k) {
    if(k == m) {
		for(int i = 0; i < m; i++) {
			cout << board[i] << ' ';
		}
		cout << endl;
		return;
	}
	
	for(int i = 0; i < n; i++) {
		if(!isused[i+1]) {
			board[k] = i+1;
			isused[i-1] = 1;
			isused[i] = 1;
			func(k+1);
			for(int j = i ; j < n; j++) {
				isused[j+1] = 0;
			}
		}
	}
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    func(0);
}
