#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<int> s;
	string text;
	int T;
	
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> text;
		if(text == "push") {
			int num;
			cin >> num;
			s.push(num);
		} else if(text == "pop") {
			if(s.empty()){
				cout << "-1" << '\n';
			} else {
				cout << s.top() << '\n';
				s.pop();
			}
		} else if(text == "size") {
			cout << s.size() << '\n';
		} else if(text == "empty") {
			if(s.empty()) cout << "1" << '\n';
			else cout << "0" << '\n';
		} else if(text == "top") {
			if(s.empty()) cout << "-1" << '\n';
			else cout << s.top() << '\n';
		}
	}
}