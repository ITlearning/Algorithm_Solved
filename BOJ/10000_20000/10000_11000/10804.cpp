#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a[20];
	int cp[20];
	int b,c;
	for(int i = 0; i < 20; i++){
		a[i] = i + 1;
		cp[i] = i + 1;
	}
	
	for(int i = 0; i < 10; i++) {
		cin >> b >> c;
		for(int j = c - 1; j >= b-1; j--) {
			cp[b+c - 2 - j] = a[j];
		}
		for(int j=0; j < 20; j++){
			a[j] = cp[j];
		}
	}
	
	for(int i = 0;i < 20; i++){
		cout << a[i] << ' ';
	}
}