#include <iostream>
#include <string>
using namespace std;

int main() {
	string text;
	getline(cin,text);
	int alpabet[26] = {0};
	for(int i = 0; i < text.length(); i++) {
		text[i] = tolower(text[i]);
		alpabet[text[i] - 97]++;
	}
	int max = 0;
	int tmp = 0;
	int flag = 0;
	for(int i = 0; i < 26; i++) {
		if(alpabet[i] > max) {
			max = alpabet[i];
			tmp = i;
			flag = 0;
		}else if (max == alpabet[i]) {
			flag = 1;
		}
 	}
	if(flag) {
		cout << "?";
	}else {
		cout << char(65 + tmp);
	}
	
}