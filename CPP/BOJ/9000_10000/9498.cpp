#include <iostream>
using namespace std;

int main() {
	int a;
	cin >> a;
	if(a >= 0 && a <= 100) {
		if(a >= 90 && a <= 100)
			cout << "A" << endl;
		else if(a >= 80 && a <= 89)
			cout << "B" << endl;
		else if(a >= 70 && a <= 79)
			cout << "C" << endl;
		else if(a >= 60 && a <= 69)
			cout << "D" << endl;
		else
			cout << "F" << endl;
	}else {
		return 0;
	}
}