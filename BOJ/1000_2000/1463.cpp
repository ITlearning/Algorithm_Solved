#include <iostream>
using namespace std;

int main() {
	int a;
	int cnt = 0;
	cin >> a;
	
	while(true) {
		if(a == 1) {
			break;
		}
		
		if(a % 3 == 0) {
			a = a / 3;
			cnt++;
		} else if (a % 2 == 0) {
			a = a / 2;
			cnt++;
		} else {
			a -= 1;
			cnt++;
		}
	}
	
	cout << cnt << '\n';
}

// 작성중