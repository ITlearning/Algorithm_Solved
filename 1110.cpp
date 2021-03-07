#include <bits/stdc++.h>
using namespace std;

int main() {
	string n;
	cin >> n;
	int a = stoi(n);
	int tmp = 0;
	int cnt = 0;
	/*while(true) {
		if(a == tmp) {
			break;
		} else {
			int t1 = n[0] - '0';
			int t2 = n[1] - '0';
			tmp = t1 + t2;
			n = n[1] + tmp;
			cnt++;
		}
	}*/
	
	int t1 = n[0] - '0';
	int t2 = n[1] - '0';
	tmp = t1 + t2;
	
	cout << tmp << endl;
	cout << n << endl;
 }