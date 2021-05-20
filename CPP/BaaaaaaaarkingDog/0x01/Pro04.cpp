#include <iostream>
using namespace std;

int func4(int N) {
	int tmp = 1;
	while(tmp*2 <= N) {
		tmp *= 2;
	}
	return tmp;
}

int main() {
	int N = 1024;
	int result = func4(N);
	cout << result << endl;
}


// O(lgN)