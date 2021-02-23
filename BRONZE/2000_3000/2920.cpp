#include <iostream>
using namespace std;

int main() {
	int fal = 0;
	int num = 0;
	for(int i = 0; i < 8; i++) {
		int tmp = num;
		cin >> num;
		
		if(tmp+1 == num) {
			fal = 1;
		} else if (tmp-1 == num) {
			fal = 2;
		} else {
			fal = 3;
		}
	}
	
	if(fal == 1)
		cout << "ascending";
	else if (fal == 2)
		cout << "descending";
	else {
		cout << "mixed";
	}
}

// 작성중