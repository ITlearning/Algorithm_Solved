#include <iostream>
#include <string>
using namespace std;
int alphabetA[26];
int alphabetB[26];
int main() {
	string textA;
	string textB;
	int cnt = 0;
	
	cin >> textA >> textB;
	for(int i = 0; i < textA.size(); i++) {
		alphabetA[textA[i] - 'a']++;
	}
	for(int i = 0; i < textB.size(); i++) {
		alphabetB[textB[i] - 'a']++;
	}
	
	for(int i = 0; i < 26; i++) {
		if(alphabetA[i] > alphabetB[i]) {
			cnt += alphabetA[i] - alphabetB[i];
		} else if (alphabetA[i] < alphabetB[i]) {
			cnt += alphabetB[i] - alphabetA[i];
		}
	}
	
	cout << cnt;
}