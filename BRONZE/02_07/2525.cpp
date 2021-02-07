#include <iostream>
using namespace std;

int main() {
	int a,b,c;
	
	cin >> a >> b >> c;
	
	b += c;
	if(b > 59) {
		a += (b/60);
		b %= 60;
	}
	
	if(a > 23) {
		a %= 24;
	}
	
	cout << a << ' ' << b << endl;
	
}