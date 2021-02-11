#include <iostream>
using namespace std;

int main() {
	int a,b,c;
	cin >> a >> b >> c;
	
	if((a > b && a < c) || (a == b && b == c)) {
		cout << a;
	}else if((b > a && b < c) || (a != b && b == c)){
		cout << b;
	}else if((c > a && c < b) || (c != a && a == b)) {
		cout << c;
	}
}