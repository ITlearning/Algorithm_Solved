#include <bits/stdc++.h>
using namespace std;

int main() {
	stack<char> s;
	string text;
	
	while(true) {
		bool t = true;
		getline(cin, text, '.');

		if(text[0] == '.') {
			cin.ignore();
			break;
		}
		for(int i = 0; i < text.length(); i++) {
			if(text[i] == '(' || text[i] == '{' || text[i] == '[') {
				s.push(text[i]);
			}
			
			if(text[i] == ')') {
				if(s.empty()){
					t = false;
					break;
				}
				char tmp = s.top();
				if(tmp == '(') {
					s.pop();
				}
			} else if (text[i] == '}') {
				if(s.empty()){
					t = false;
					break;
				}
				char tmp = s.top();
				if(tmp == '{') {
					s.pop();
				}
			} else if (text[i] == ']') {
				if(s.empty()){
					t = false;
					break;
				}
				char tmp = s.top();
				if(tmp == '[') {
					s.pop();
				}
			}
		}
		
		if(t) {
			if(!s.empty()) {
				cout << "no" << endl;
			} else {
				cout << "yes" << endl;
			}
		} else {
			cout << "no" << endl;
		}
		
	}
	
	
}