#include <iostream>
#include <string>
using namespace std;

int main() {
	string S;
	string alpa = "abcdefghijklmnopqrstuvwxyz";
	
	cin >> S;
	for(int i = 0; i < alpa.length(); i++) {
		cout << (int)S.find(alpa[i]) << " ";
	}
}