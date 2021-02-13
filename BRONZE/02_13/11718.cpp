#include <iostream>
#include <string>
using namespace std;

int main() {
	string h;
	
	while(true) {
		getline(cin,h);
		if(h == "")
			break;
		cout << h << endl;
	}
	
	
}