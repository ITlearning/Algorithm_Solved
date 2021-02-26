#include <iostream>
using namespace std;

int main() {
	int a,b;
	cin >> a >> b;
	if(0 < a && b < 10) {
		cout.precision(10);
		cout << a/(long double)b << endl;
	}else {
		return 0;
	}
	
}