#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int a[5], mid, tmp;
	tmp = 0;
	for(int i = 0; i < 5; i++) {
		cin >> a[i];
		tmp += a[i];
	}
	sort(a, a+5);
	
	mid = a[2];
	cout << tmp/5 << '\n' << mid;
}