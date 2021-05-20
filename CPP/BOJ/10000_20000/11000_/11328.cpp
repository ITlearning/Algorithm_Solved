#include <iostream>
#include <string>
using namespace std;

int func(string a, string b) {
	int alphaA[26] = {};
	int alphaB[26] = {};
	
	for(int i = 0; i < a.size(); i++) {
		alphaA[a[i] - 'a']++;
		alphaB[b[i] - 'a']++;
	}
	
	for(int i = 0; i < 26; i++) {
		if(alphaA[i] != alphaB[i]) {
			return 0;
		}
	}
	return 1; 
}
	


int main() {
	string a;
	string b;
	
	int N;
	cin >> N;
	
	for(int i = 0; i < N; i++) {
		cin >> a >> b;
		int result = func(a,b);
		if(result == 0) {
			cout << "Impossible";
		} else if (result == 1){
			cout << "Possible";
		}
		cout << '\n';
	}
}