#include <iostream>
using namespace std;

int main() {
	int a[9];
	
	for(int i = 0; i < 9; i++) {
		cin >> a[i];
	}
	int max = 0;
	int number = 1;
	for(int i = 0; i < 9; i++) {
		if(max < a[i]) {
			max = a[i];
			number = i + 1;
		}
		
	}
	
	cout << max << '\n';
	cout << number;
}