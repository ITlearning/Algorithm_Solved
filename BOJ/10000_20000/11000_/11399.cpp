#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N;
	int total = 0;
	cin >> N;
	int num[N] = {0};
	for(int i = 0; i < N; i++) {
		cin >> num[i];
	}
	total = num[0];
	for(int i = 1; i < N; i++) {
		total += num[i];
	}
	
	cout << total << '\n';
}

// 작성중