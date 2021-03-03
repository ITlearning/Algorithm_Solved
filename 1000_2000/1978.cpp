#include <iostream>
using namespace std;

bool isPrime(int num) {
	if(num < 2) return false;
	for(int i = 2; i*i <= num; i++) {
		if(num % i == 0) return false;
	}
	return true;
}

int main() {
	int N = 0;
	cin >> N;
	int count = 0;
	for(int i = 0; i < N; i++) {
		int num;
		cin >> num;
		if(isPrime(num)) {
			count++;
		}
	}
	cout << count << endl;
	
}