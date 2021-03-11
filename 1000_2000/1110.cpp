#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	int t1;
	int t2;

	int tmp = 0;
	int result = 0;
	int cnt = 0;
	
	cin >> n;
	
	if(n < 10) {
		n *= 10;
	}
	
	result = n;
	
	while(true) {
		t1 = result / 10;
		t2 = result % 10;
		tmp = t1 + t2;
		result = (t2 * 10) + (tmp % 10);
		cnt++;
		
		if(n == result) {
			break;
		}
	}
	
	cout << cnt << endl;
 }