#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	deque<int> dq;
	int t;
	
	cin >> t;
	while(t--) {
		string c;
		cin >> c;
		if(c == "push_front") {
			int num;
			cin >> num;
			dq.push_front(num);
		} else if(c == "push_back") {
			int num;
			cin >> num;
			dq.push_back(num);
		} else if(c == "pop_front") {
			if(dq.empty()) cout << "-1" << '\n';
			else {
				cout << dq.front() << '\n';
				dq.pop_front();
			}
		} else if(c == "pop_back") {
			if(dq.empty()) cout << "-1" << '\n';
			else {
				cout << dq.back() << '\n';
				dq.pop_back();
			}
		} else if(c == "size") {
			cout << dq.size() << '\n';
		} else if(c == "empty") {
			if(dq.empty()) cout << "1" << '\n';
			else cout << "0" << '\n';
		} else if(c == "front") {
			if(dq.empty()) cout << "-1" << '\n';
			else cout << dq.front() << '\n';
		} else if(c == "back") {
			if(dq.empty()) cout << "-1" << '\n';
			else cout << dq.back() << '\n';
		}
	}
}