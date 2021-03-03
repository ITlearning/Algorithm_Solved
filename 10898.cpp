#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	
	
	int* v;
	int T;
	cin >> T;
	int arr[10001] = {0};
	v = new int[T];
	for(int i = 0; i < T; i++) {
		int num;
		cin >> num;
		arr[num] += 1;
	}
	
	for(int i = 0; i < 10000; i++) {
		for(int j = 0; j < arr[i]; j++) {
			cout << i << '\n';
		}
	}
}