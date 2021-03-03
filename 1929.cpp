#include <iostream>
using namespace std;

void isPrime(int start, int endnum) {
	if(start < start) cout << start << endl;
	for(int i = start; i*i <= endnum; i++) {
		if(endnum % i == 0) cout << i << endl;
	}
}

int main() {
	int start;
	int endnum;
	cin >> start >> endnum;
	
	isPrime(start, endnum);
	
	
}