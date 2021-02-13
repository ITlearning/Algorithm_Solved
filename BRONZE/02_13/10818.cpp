#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int a;
	int b;
	int min = 0;
	int max = 0;
	cin >> a;
	for(int i = 0; i < a; i++) {
		cin >> b;
		
		if(min >= b) {
			min = b;
		} else if (min == 0) {
			min = b;
		}
		
		if(max <= b) {
			max = b;
		} else if(max == 0) {
			max = b;
		}
	}
	
	cout << min << ' ' << max << endl;
}