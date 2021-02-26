#include <iostream>
using namespace std;

int main() {
	int N;
	int a, b;
	cin >> N;
	if(N > 10) {
		a = N / 5;
		b = (N - (a * 5)) / 3;
		if(b % 3 != 0) {
			b = b % 3;
		}
	} else {
		b = N / 3;
	}
	
	
	cout << a << endl;
	cout << b <<endl;
}