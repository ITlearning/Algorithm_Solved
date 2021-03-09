#include <bits/stdc++.h>
using namespace std;

int main() {
	string n;
	string b;
	cin >> n;
	bool t = false;
	int a = stoi(n);
	int tmp = 0;
	int cnt = 0;
	while(true) {
		if(n == to_string(a) && t == true) {
			break;
		} else {
			if()
			t = true;
			int t1 = n[0] - '0';
			int t2 = n[1] - '0';
			tmp = (t1 + t2) % 10;
			n = to_string(t2) + to_string(tmp);
			cnt++;
		}
	}
	
	cout << cnt << endl;
 }