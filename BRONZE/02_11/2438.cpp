#include <iostream>
using namespace std;

int main() {
	int a;
	int j = 0;
	cin >> a;
	for(int i = 0; i < a; i++) {
		j = 0;
		for(; j < i + 1; j++) {
			cout << "*";
		}
		cout << endl;
	}
}