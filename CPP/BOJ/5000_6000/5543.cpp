#include <iostream>
using namespace std;

int main() {
	int buger[3];
	int coke[2];
	int min = 9999;
	int minc = 9999;
	for(int i = 0; i < 3; i++) {
		cin >> buger[i];
		if(buger[i] < min) {
			min = buger[i];
		}
	}
	
	for(int i = 0; i < 2; i++) {
		cin >> coke[i];
		if(coke[i] < minc) {
			minc = coke[i];
		}
	}
	
	
	cout << min + minc - 50 << endl;
}