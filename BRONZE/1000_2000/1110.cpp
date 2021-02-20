#include <iostream>
#include <string>
using namespace std;

void newMath(char a) {
	char *p = &a;
	int c = 0;
	
	int cnt =0;
	while(p[c] != '\0') {
		cout << p[c] << endl;
		c++;
		if(c == 2) {
			break;
		}
	}
}

int main() {
	char a[];
	for(in)
	cin >> a;
	newMath(a);
}