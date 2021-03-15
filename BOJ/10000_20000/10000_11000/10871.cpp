#include <iostream>
using namespace std;

int main() {
	int a;
	int x;
	cin >> a >> x;
	int N[a];
	for(int i = 0; i < a; i++) {
		cin >> N[i];
	}
	
	for(int i = 0; i < a; i++) {
		if(N[i] < x) {
			cout << N[i] << ' ';
		}
	}
}