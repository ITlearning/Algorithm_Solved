#include <iostream>
using namespace std;

int main() {
	int a,b;
	int c,d,e;
	int result;
	cin >> a >> b;
	result = a * b;
	c = a * (b % 10);
	d = a * ((b/10) % 10);
	e = a * (((b/10)/ 10) % 10);
	
	cout << c << '\n' << d << '\n' << e << '\n' << result;

}