#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<char> s;
	string text;
	long long result = 0;
	int tmp = 1;
	bool impossible = false;
	
	cin >> text;
	for(int i = 0; i < text.size(); i++) {
		if(text[i] == '(') {
			tmp *= 2;
			s.push(text[i]);
			
		}
		else if(text[i] == '[') {
			tmp *= 3;
			s.push(text[i]);
			
		}
		else if(text[i] == ')' && (s.empty() || s.top() != '(')) {
			impossible = true;
			break;
		}
		else if(text[i] == ']' && (s.empty() || s.top() != '[')) {
			impossible = true;
			break;
		}
		else if(text[i] == ']') {
			if(text[i-1] == '[') {
				result += tmp;
			}
			s.pop();
			tmp /= 3;
		}
		else if(text[i] == ')') {
			if(text[i-1] == '(') {
				result += tmp;
			}
			s.pop();   
			tmp /= 2;
		}
	}

	
	if(impossible || !s.empty()) {
		cout << "0" << endl;
	} else {
		cout << result << endl;
	}
}