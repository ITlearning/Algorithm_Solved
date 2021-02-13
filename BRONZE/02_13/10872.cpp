#include <iostream>
using namespace std;

int fac(int x) {
	if(x <= 1) return 1;
	else return x * fac(x - 1);
} // 재귀함수

int main() {
	int num;
	cin >> num;
	cout << fac(num) << '\n';
}