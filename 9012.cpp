// 작성중

#include <iostream>
#include <string>
using namespace std;

int main() {
	int L = 0;
	int R = 0;
	int t = 0;
	string VPS;
	cin >> t;
	for(int i = 0; i < t; i++) {
		L = 0;
		R = 0;
		cin >> VPS;
		
		for(int j = 0; j < VPS.size(); j++) {
			if(VPS[j] == '(') {
				L++;
			} else {
				R++;
			}
		}
		if(L == R) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
}