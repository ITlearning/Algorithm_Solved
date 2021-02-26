#include <iostream>
using namespace std;

int main() {
	int a = 0;
	int div[42] = {0};
	int cnt = 0;
	for(int i = 0; i < 10; i++) {
		cin >> a;
		if(!div[a % 42]++) {
			cnt++;
		}
	}
	cout << cnt << '\n';
}