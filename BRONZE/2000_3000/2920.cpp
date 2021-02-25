#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int oct[8];
	int fal = 0;
	int dal = 0;
	for(int i = 0; i < 8; i++) {
		cin >> oct[i];
		
		if(oct[i] == i + 1) {
			fal++;
		} else if (oct[i] == 8 - i) {
			dal++;
		}
	}
	
	
	if(fal == 8) {
		cout << "ascending" << endl;
	} else if (dal == 8){
		cout << "descending" << endl;
	} else {
		cout << "mixed" << endl;
	}
}

// 작성중