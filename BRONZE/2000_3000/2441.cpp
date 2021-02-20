#include <iostream>
using namespace std;

int main() {
	int n;
	int j = 0;
	int k = 5;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		j = 0;
		for(; j < i; j++) {
			cout << " ";
		}
		for(int j = 0; j < n - i; j++) {
			cout << "*";
		}
		cout << '\n';
	}
}