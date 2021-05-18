#include <bits/stdc++.h>
using namespace std;

int board[1502];
int tmp[1502];
int n;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	int maxi = 0;
	for(int i = 0; i < n*n; i++) {
		cin >> board[i];
	}
	
	sort(board, board+n*n);
	
	cout << board[n-1] << endl;
}