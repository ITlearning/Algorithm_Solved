#include <bits/stdc++.h>
using namespace std;
// N 부터 1까지의 수 출력
/*
void recursion(int a) {
	if(a == 1) {
		cout << a << endl;
	}else {
		cout << a << endl;
		recursion(a-1);
	}
}
*/


// 1부터 N까지의 합 출력

int recursion(int a) {
	if(a==0) return 0;
	
	return a+recursion(a-1);

}

int main() {
	int b = recursion(10);
	cout << b << endl;
}