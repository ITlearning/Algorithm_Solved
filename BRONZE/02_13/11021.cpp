#include <iostream>
using namespace std;

int main() {
	int t;
	int a,b;
	
	cin >> t;
	int numA[t];
	int numB[t];
	for(int i = 0; i < t; i++) {
		cin >> numA[i] >> numB[i];
	}
	
	for(int i = 0; i< t; i++) {
		cout << "Case #" << i + 1 << ": " << numA[i] + numB[i] << '\n';
	}
}