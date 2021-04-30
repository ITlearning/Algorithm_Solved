#include <bits/stdc++.h>
using namespace std;

int main() {
	int ax = 5;
	int ac[2] = {-1, 1}; 
	int cnt = 0;
	while(ax > 0 && ax <= 10) {
		ax += ac[1];
		cout << cnt++ << endl;
	}
}