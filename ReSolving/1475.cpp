#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int num[10];
int main() {
	string a;
	int set_case = 0;
	cin >> a;
	
	for(int i = 0; i < a.size(); i++) {
		num[a[i] - '0']++;
	}
	int tmp = 0;
	for(int i = 0; i < 10; i++) {
		if(i!=9 && i!=6) tmp = max(tmp,num[i]);
	}
	cout << max(tmp, (num[6] + num[9] + 1)/2);
}