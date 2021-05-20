#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n = 9;
	int a[9], tmp;
	tmp = 0;
	for(int i = 0; i < n; i++) {
		cin >> a[i];
		tmp += a[i];
	}
	
	sort(a, a+n);
	
	for(int i = 0; i < n; i++) {
		for(int j = i + 1; j < n; j++) {
			if(tmp - a[i] - a[j] == 100) {
				for(int k = 0; k < n; k++) {
					if(i == k || j == k) continue;
					cout << a[k] << '\n';
				}
				return 0;
			}
			
		}
	}
	return 0;
}


// 브루트 포스 알고리즘