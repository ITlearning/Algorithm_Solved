#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<int> s;
	int k;
	cin >> k;
	for(int i = 0; i < k; i++) {
		int num;
		cin >> num;
		if(num == 0) {
			s.pop();
		} else {
			s.push(num);
		}
	}
	int total = 0;
	while(!s.empty()) {
		total += s.top();
		s.pop();
	}
	cout << total;
}