#include <iostream>
using namespace std;

int main() {
	int a,b[5];
	int cnt = 0;
	cin >> a;
	
	for(int i= 0; i < 5; i++) {
		cin >> b[i];
	}
	
	for(int i = 0; i < 5; i++) {
		if(a == b[i]) {
			cnt++;
		}
	}
	
	cout << cnt << endl;
}