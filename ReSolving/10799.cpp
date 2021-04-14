#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<char> s;
	int result = 0;
	string gual;
	cin >> gual;
	for(int i = 0; i < gual.length(); i++) {
		if(gual[i] == '(') {
			s.push(gual[i]);
		} else {
			s.pop();
			if(gual[i-1] == '(') {
				result += s.size();
			} else {
				result++;
			}
		}
	}
	
	
	cout <<result << endl;
}