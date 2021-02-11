#include <iostream>
using namespace std;

int main() {
	int a;
	int b = 0;
	cin >> a;
	if(a > 100000) {
		return 0;
	}else {
		while(b < a) {
		++b;
		cout << b << endl;
		
		}
	}
	
}