#include <bits/stdc++.h>
using namespace std;

int main() {
	stack<char> s;
	int total = 0;
	int tmpx = 1;
	int tmpy = 1;
	string text;
	cin >> text;
	for(int i = 0; i < text.length(); i++) {
		if(text[i] == '(') {
			s.push(text[i]);
			tmpx *= 2;
		} else if (text[i] == '[') {
			s.push(text[i]);
			tmpy *= 3;
		} else {
			s.pop();
			if(text[i-1] == '(' && s.empty() == 0) {
				tmpx /= 2;
			} else if (text[i - 1] == ']' && s.empty() == 0) {
				tmpy /= 3;
			} else if (s.empty()) {
				if(text[i] == ')') {
					total += tmpx * 2;
				} else if (text[i] == ']') {
					total += tmpy * 3;
				}
			}
 		}
	}
	
	if(!s.empty()) {
		cout << "0" << endl;
	} else {
		cout << total << endl;
	}
}