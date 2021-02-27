#include <iostream>
#include <string>
using namespace std;

int main() {
	string number;
	int to = 0;
	getline(cin, number);
	for(int i = 0; i < number.size(); i++) {
		if(number[i] == '1') {
			to += 2;
		} else {
			if(number[i] >= 'A' &&  number[i] <= 'C') {
				to += 3;
			} else if (number[i] >= 'D' &&  number[i] <= 'F') {
				to += 4;
			} else if (number[i] >= 'G' &&  number[i] <= 'I') {
				to += 5;
			} else if (number[i] >= 'J' &&  number[i] <= 'L') {
				to += 6;
			} else if (number[i] >= 'M' &&  number[i] <= 'O') {
				to += 7;
			} else if (number[i] >= 'P' &&  number[i] <= 'S') {
				to += 8;
			} else if (number[i] >= 'T' &&  number[i] <= 'V') {
				to += 9;
			} else if (number[i] >= 'W' &&  number[i] <= 'Z') {
				to += 10;
			} else {
				to += 11;
			}
		}
	}
	
	cout << to << '\n';
}