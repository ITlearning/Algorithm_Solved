#include <iostream>
using namespace std;

int fibo(int num) {
	if(num == 0)
		return 0;
	else if (num == 1)
		return 1;
	else
		return fibo(num-1) + fibo(num-2);
}

int main() {
	int n;
	cin >> n;
	cout << fibo(n) << '\n';
	
	
	return 0;
}