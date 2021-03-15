#include <iostream>
using namespace std;

int main() {
	int a;
	int b = 0;
	cin >> a;
	if(a > 100000) {
		return 0;
	}else {
		for(int i = a; i > b; i--) {
			cout << i << '\n';
		}
	}
	
}