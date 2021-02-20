#include <iostream>
using namespace std;

int main() {
	int t;
	int num = 0;
	int a,b,c;
	cin >> t;
	a = 0;
	b = 0;
	c = 0;
	if(t >= 300) {
		a = t / 300;
		t %= 300;
	} 
	
	if( t >= 60) {
		b = t / 60;
		t %= 60;
	}
	
	if( t >= 10) {
		c = t / 10;
		t %= 10;
	}
	
	if(t != 0) {
		cout << "-1" << endl;
	} else {
		cout << a << ' ' << b << ' ' << c << endl;
	}
	
	
	
}