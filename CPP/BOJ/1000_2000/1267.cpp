#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int n, M,Y;
	cin >> n;
	int *a;
	a = new int [n];
	int tmp = 0;
	M = 0;
	Y = 0;
	for(int i =1; i <=n; i++) {
		cin >> a[i];
		M += (a[i]/60 + 1) * 15;
		Y += (a[i]/30 + 1) * 10;
	}
	
	if(M < Y) {
		cout << "M " << M;
	} else if (M > Y) {
		cout << "Y " << Y << '\n';
	} else {
		cout << "Y M " << Y << '\n';
	}
	
}