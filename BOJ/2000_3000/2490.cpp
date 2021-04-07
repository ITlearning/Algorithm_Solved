#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int a[4],b[4],c[4], cnt;
	cnt = 0;
	for(int i = 0; i < 3; i++) {
		for (int j = 0; j < 4; j++) {
			if(i == 0) {
				cin >> a[j];
			} else if (i == 1) {
				cin >> b[j];
			} else {
				cin >> c[j];
			}
		}
	}
	
	for(int i = 0; i < 3; i++) {
		cnt = 0;
		for (int j = 0; j < 4; j++) {
			if(i == 0) {
				if(a[j] == 0){
					cnt++;
				}
			} else if (i == 1) {
				if(b[j] == 0) {
					cnt++;
				}
			} else {
				if(c[j] == 0) {
					cnt++;
				}
			}
		}
		if(cnt == 0) {
			cout << "E" << '\n';
		} else if (cnt == 1) {
			cout << "A" << '\n';
		} else if (cnt == 2) {
			cout << "B" << '\n';
		} else if (cnt == 3) {
			cout << "C" << '\n';
		} else if (cnt == 4) {
			cout << "D" << '\n';
		}
	}
}