#include <iostream>
using namespace std;

int main() {
	int k,n,m;
	int sum;
	cin >> k >> n >> m;
	sum = k * n;
	
	if(sum > m) {
		cout << sum - m << endl;
	} else {
		cout << "0" << endl;
	}
	
	
}