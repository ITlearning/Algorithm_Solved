#include <bits/stdc++.h>
using namespace std;

// 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력하는 함수
void func(int a, int b, int n) {
	if(n == 1){
		cout << a << ' ' << b << '\n';
		return;
	}
	func(a,6-a-b, n-1);
	cout << a << ' ' << b << '\n';
	func(6-a-b, b, n-1);
}

int main() {
	int t = 0;
	cin >> t;
	cout << (1<<t) - 1 << '\n';
	func(1,3,t);
}