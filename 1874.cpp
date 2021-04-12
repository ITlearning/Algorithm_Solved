#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	char text[200050];
	int p = 0;
	int n, x, max = 0;
	cin >> n;
	stack<int> s;
	while(n--) {
		cin >> x;
		if(x > max) {
			for(int i = max + 1; i <= x; i++) {
				s.push(i);
				text[p++] = '+';
			}
		} else {
			if(s.top() != x) {
				cout << "NO";
				return 0;
			}
		}
		s.pop();
		text[p++] = '-';
		if(max < x) max = x;
	}
	for(int i = 0; i < p; i++) cout << text[i] << '\n';
}