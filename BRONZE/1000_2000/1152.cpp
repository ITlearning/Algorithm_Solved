#include <iostream>
#include <string>
using namespace std;

int main() {
	string a;
	int cnt = 0;
	getline(cin,a);
	
	for(int i = 0; i < a.length(); i++) {
		if(a[i-1] != ' ' && a[i] == ' ') {
			if(i != 0 && i != a.length()-1) {
				cnt++;	
			} else {
				cnt = cnt;
			}
		}
		
	}
	if(a[0] == ' ' && a.length() == 1) {
		cout << 0;
	} else
		cout << cnt + 1;
	
}


// 문제 풀이중