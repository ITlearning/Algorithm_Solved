#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	queue<int> q;
	int t;

	string con;
	cin >> t;
	while(t--) {
		cin >> con;
		if(con == "push") {
			int num;
			cin >> num;
			q.push(num);
		} else if(con == "pop") {
			if(q.empty()) cout << "-1" << '\n';
			else {
				cout << q.front() << '\n';
				q.pop();
			}
		} else if(con == "size") {
			cout << q.size() << '\n';
		} else if(con == "empty") {
			if(!q.empty()) {
				cout << "0" << '\n';
			} else {
				cout << "1" << '\n';
			}
		} else if(con == "front") {
			if(q.empty()) cout << "-1" << '\n';
			else cout << q.front() << '\n';
		} else if(con == "back") {
			if(q.empty()) cout << "-1" << '\n';
			else cout << q.back() << '\n';
		}
	}
}