#include <iostream>
#include <string>
using namespace std;

int main() {
	string text;
	getline(cin, text);
	
	for(int i = 0; i < text.size(); i++) {
		cout << text[i];
		if((i+1) % 10 == 0) {
			cout << '\n';
		}
	}
	
	return 0;
}