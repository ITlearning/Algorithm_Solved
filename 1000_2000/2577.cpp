#include <iostream>
#include <string>
using namespace std;

int main() {
	int a;
	int b;
	int c;
	int cnt[10] = {0, };
	char num;
	cin >> a >> b >> c;
	int total = a * b * c;
	
	while(total != 0) {
		cout << total / 10 << endl;
	}
	
	cout << num << endl;
}