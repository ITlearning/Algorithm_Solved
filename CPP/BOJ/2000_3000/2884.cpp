#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
	int H, M;
	int ff = 45;
	
	cin >> H >> M;
	int tmp = M - ff;
	if(tmp < 0) {
		H -= 1;
		if(H < 0) {
			H = 24 - abs(H);
		}
		M = 60 - abs(tmp);
	} else {
		M = tmp;
	}
	
	cout << H << ' ' << M << '\n';
}