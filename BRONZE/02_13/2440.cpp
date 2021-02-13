#include <iostream>
using namespace std;

int main() {
	int a,j;
	cin >> a;
	
	for(int i = 0; i < a; i++) {
		
		for(j = i; j < a; j++) {
			cout << "*";
		}
		cout << '\n';
	}
}