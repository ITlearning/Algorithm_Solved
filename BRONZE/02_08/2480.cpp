#include <iostream>
using namespace std;

int main() {
	int b1,b2,b3;
	cin >> b1 >> b2 >> b3;
	if(b1 == b2 && b2 == b3) {
		cout << 10000 + b1 * 1000 << endl;
	} else if (b1 == b2 || b1 == b3 || b2 == b3) {
		if(b1 == b2 || b2 == b3) {
			cout << 1000 + b2 * 100 << endl;
		} else {
			cout << 1000 + b3 * 100 << endl;
		}
	} else {
		if(b1 > b2 && b1 > b3) {
			cout << b1 * 100 << endl;
		} else if(b2 > b1 && b2 > b3) {
			cout << b2 * 100 << endl;
		} else {
			cout << b3 * 100 << endl;
		}
	}
}