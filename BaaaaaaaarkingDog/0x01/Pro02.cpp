#include <iostream>
using namespace std;

int func2(int arr[], int N) {
	int t;
	for(int i = 0; i < N; i++) {
		for(int j = i; j < N; j++){
			if(arr[i] + arr[j + 1]== 100) {
				return 1;
			}
		}
	}
	return 0;
}

int main() {
	int arr[] = {4,13,63,87};
	int n = 4;
	int result = func2(arr,n);
	cout << result << endl;
}