#include <iostream>
#include <string>
using namespace std;

int main() {
	
	int T;
	cin >> T;
	string OX;
	for(int i = 0; i < T; i++) {
		cin >> OX;
		int cnt = 0;
		int sum = 0;
		for(int j = 0; j < OX.length(); j++) {
			if(OX[j] == 'O') cnt++;
			else cnt = 0;
			sum += cnt;
		}
		
		cout << sum << '\n';
	}
}