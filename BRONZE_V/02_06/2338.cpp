#include <iostream>
using namespace std;

int main() {
	int a, b;
	cin >> a;
	cin >> b;
	
	if(a > 1000 || b > 1000) {
		return 0;
	}else {
		cout << a + b << endl;
		cout << a - b << endl;
		cout << a * b << endl;
	}
	
}