#include <iostream>
using namespace std;

int main() {
	int t;
	int a, b;
	
	cin >> t;
	int A[t], B[t];
	for(int i = 0; i < t; i++) {
		cin >> A[i] >> B[i];
	}
	
	for(int i = 0; i < t; i++) {
		cout << A[i] + B[i] << '\n';
	}
}