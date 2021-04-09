#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string text;
	int number[26] = {0,};
	getline(cin, text, '\n');
	
	for(int i = 0; i < text.size(); i++) {
		number[text[i] - 'a']++;
	}
	
	
	for(int i = 0; i < 26; i++) {
		cout << number[i] << ' ';
	}
}