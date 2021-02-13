#include <iostream>
using namespace std;

int main() {
	int a, b;
	int cnt = 0;
	while(true) {
		cin >> a >> b;
		if(a == 0 && b == 0) {
			break;
		} else {
			cout << a + b << '\n';
		}
	}
}