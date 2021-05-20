#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int num;
	cin >> num;
	
	for(int i = 1; i < num; i++){
		int j = 1;
		for(int k = i; k < num; k++){
			cout << ' ';
		}
		for(; j <= 2*i-1; j++) {
			cout << "*";
		}
		cout << '\n';
	}
	
	for(int i = num; i >= 1; i--) {
		int k = 1;
		for(; k <= num - i; k++) {
			cout << ' ';
		}
		
		int j = 2*i-1;
		for(; j >= 1; j--) {
			cout << "*";
		}
		cout << '\n';
	}
}