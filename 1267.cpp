#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int n, M,Y;
	cin >> n;
	int a[n];
	int tmp = 0;
	M = 0;
	Y = 0;
	for(int i = 0;i < n; i++) {
		cin >> a[i];
	}
	
	for(int i = 0 ; i < n; i++) {
		tmp += a[i];
		if(a[i] > 30) {
			M += 10;
		}
	}
	
	for(int i = 0; i < n; i++) {
		tmp += a[i];
		if(a[i] > 60) {
			Y += 15;
		}
	}
	
	Y += 15 *(tmp / 60);
	M += 10 *(tmp / 30);
	
	if(Y < M) {
		cout << "Y" << '\n' << Y << '\n';
	} else if (Y > M){
		cout << "M" << '\n' << M << '\n';
	} else {
		cout << "Y M " << M << '\n';
	}
}