#include <bits/stdc++.h>
using namespace std;
stack<char> s;
string text;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int p = 1;
	while(true) {
		
		int cnt = 0;
		cin >> text;
		
		for(int i = 0; i < text.size(); i++) {
			char c = text[i];
			if(c == '{') {
				s.push(c);
			} else if(c == '}') {
				if(s.empty() || s.top() != '{') {
					s.push(c);
				} else {
					s.pop();
				}
				
			} else {
				return 0;
			}
		}
		while(!s.empty()) {
			char t = s.top();
			s.pop();
			if(s.top() != t) {
				cnt += 2;
			} else {
				cnt += 1;
			}
			s.pop();
		}
		
		cout << p++ << ". " << cnt << '\n';
	}
	
}