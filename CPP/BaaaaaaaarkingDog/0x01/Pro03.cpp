#include <iostream>
using namespace std;

int func3(int N){
	for(int i = 1; i <= N; i++) {
		if(i * i == N) {
			return 1;
		}
	}
	return 0;
}

int main() {
	int N = 756580036;
	int result = func3(N);
	cout << result << endl;
}

// O(/N)