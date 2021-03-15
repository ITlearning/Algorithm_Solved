#include <string>
#include <iostream>
using namespace std;

int main() {
	string a;
	int count = 0;
	while(getline(cin, a, '\n')) {
		if(count > 100) {
			break;
		}
		cout << a;
		count++;
	}
}