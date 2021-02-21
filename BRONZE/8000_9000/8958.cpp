#include <iostream>
#include <string>
using namespace std;

int main() {
	int tmp = 0;
	int T;
	cin >> T;
	string OX;
	int cnt[T] = {0};
	for(int i = 0; i < T; i++) {
		cin >> OX;
		for(int j = 0; j < OX.length(); j++) {
			if(OX[i] == 'O') {
				int x = i;
				while(OX[x] == 'O') {
					tmp = tmp + 1;
					--x;
				}
				cnt[i] += tmp;
				tmp = 1;
			}
			
		}
	}
	
	for(int i = 0; i < T; i++) {
		cout << cnt[i] << '\n';
	}
}