#include <iostream>
#include <string>
using namespace std;
int main(void) {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int n; string s;
		cin >> n >> s;
		for (int i = 0; i < s.length(); i++) {
			for (int j = 0; j < n; j++) {
				cout << s[i];
			}
		}
		cout << endl;
	}
}

// 작성중

