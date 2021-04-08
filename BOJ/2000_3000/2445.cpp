#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int num;
	cin >> num;
	for(int i = 1; i <= num; i++){
		for(int j = 1; j <= i; j++) {
			cout << "*";
		}
		for(int j = 1; j <= 2*(num-i); j++) {
			cout << ' ';
		}
		for(int j = 1; j <= i; j++) {
			cout << "*";
		}
		cout << '\n';
	}
	
	for(int i = 1; i <= num-1; i++) {
		for(int j = i; j < num; j++) {
			cout << "*";
		}
		for(int j = 1; j <= i*2; j++) {
			cout << ' ';
		}
		for(int j = i; j < num; j++) {
			cout << "*";
		}
		cout << '\n';
	}
}