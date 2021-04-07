#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	long long a,b,c;
	cin >> a >> b;
	if(a < b) {
		c = b - a - 1;
		cout << c << '\n';
		for(long long i = a; i < b-1; i++) {
			cout << i + 1 << ' ';
		}
	}else if(a > b){
		c = a - b - 1;
		cout << c << '\n';
		for(long long i = b; i < a-1; i++) {
			cout << i + 1 << ' ';
		}
	} else if (a == b){
		c = 0;
		cout << c << '\n';
	}
	
	
}