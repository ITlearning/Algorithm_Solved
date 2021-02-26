#include <iostream>
using namespace std;

int main() {
	int a[5];
	int avg = 0;
	for(int i = 0; i < 5; i++) {
		cin >> a[i];
	}
	
	for(int i= 0; i< 5; i++) {
		if(a[i] < 40) {
			a[i] = 40;
		}
	}
	
	for(int i = 0; i < 5; i++) {
		avg += a[i];
	}
	
	cout << avg / 5 << endl;
}