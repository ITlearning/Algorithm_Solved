#include <iostream>
using namespace std;

int main() {
	int a;
	int total = 0;
	for(int i = 0; i < 5; i++){
		cin >> a;
		total += a*a;
	}
	
	cout << total % 10 <<'\n';
}