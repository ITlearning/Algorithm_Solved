#include <iostream>
using namespace std;

int func2(int arr[], int N) {
	int index[101] = {0,};
	for(int i = 0; i < N; i++) {
		if(index[100 - arr[i]] == 1) {
			return 1;
		}
		index[arr[i]] = 1;
	}
	return 0;
}

int main() {
	int arr[] = {50,42};
	int n = 2;
	int result = func2(arr,n);
	cout << result << endl;
}