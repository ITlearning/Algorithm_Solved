#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int a,b,tmp;
	b = 0;
	tmp = 0;
	for(int i = 0; i < 7; i++) {
		cin >> a;
		if(a % 2 == 1) {
			b += a;
			if(tmp == 0) {
				tmp = a;
			} else if(tmp > a) {
				tmp = a;
			}
		}
	}
	if(b == 0) {
		cout << "-1";
	}else {
		cout << b << '\n' << tmp << '\n';
	}
	
}