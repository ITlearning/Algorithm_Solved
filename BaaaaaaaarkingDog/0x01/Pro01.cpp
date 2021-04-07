#include <iostream>
using namespace std;

int func1(int N) {
	int tmp = 0;
	for(int i = 1; i <= N; i++) {
		if(i % 3 == 0 || i & 5 == 0) {
			tnp += i;
		}
	}
	
	return tmp;
}

int main() {
	int a;
	int result = func1(a);
	cout << result << endl;
} 