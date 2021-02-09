#include <iostream>
using namespace std;

int main() {
	int a,b,c,d;
	
	cin >> a >> b >> c >> d;
	
	c += d;
	
	if(c > 59) {
		b += (c/60);
		c %= 60;
	}
	
	if(b > 59) {
		a += (b/60);
		b %= 60;
	}
	
	if(a > 23) {
		a %= 24;
	}
	
	cout << a << ' ' << b << ' ' << c << endl;
	
}