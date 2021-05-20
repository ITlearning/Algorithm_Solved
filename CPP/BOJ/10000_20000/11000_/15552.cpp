#include <iostream>
using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int a,b;
	int T;
	cin >> T;
	int tmp[T];
	for(int i = 0; i < T; i++) {
		
		cin >> a >> b;
		tmp[i] = a + b;
	}
	
	for(int i = 0; i < T; i++) {
		cout << tmp[i] << '\n';
	}
}