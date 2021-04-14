#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	while(true) {
		bool t = false;
		string text;
		stack<char> s;
		getline(cin, text);

		if(text.size() == 1 &&text[0] == '.') {
			break;
		}
		for(int i = 0; i < text.length(); i++) {
			if(text[i] == '(' || text[i] == '[') {
				s.push(text[i]);
			} else {
					if(text[i] == ')') {
					if(s.size() > 0 && s.top() == '(') {
						s.pop();
					} else {
						t = true;
						break;
						}
					} else if (text[i] == ']') {
					if(s.size() > 0 && s.top() == '[') {
						s.pop();
					} else {
						t = true;
						break;
					}
				}
			}
			
			
		}
		
		if(s.empty() > 0 && !t) {
			cout << "yes" << '\n';
		} else {
			cout << "no" << '\n';
		}
 		
	}
	
	
}