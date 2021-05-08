#include <bits/stdc++.h>
using namespace std;

int main() {
	list<char> L;
	list<char>::iterator t = L.begin();
	string text;
	char control;
	char alphabet;
	int num;
	cin >> text;
	for(int i = 0; i < text.size(); i++) {
		char a = text[i];
		L.push_back(a);
		//t++;
	}
	//t++;
	cin >> num;
	for(int i = 0; i < num; i++) {
		cin >> control;
		if(control == 'L') {
			if(t != L.begin()) {
				t--;
				continue;
			}
			continue;
		} else if(control == 'D') {
			if(t != L.end()) {
				t++;
				continue;
			}
			continue;
		} else if(control == 'B') {
			if(t == L.begin()) {
				continue;
			}else {
				t--;
				t = L.erase(t);
				continue;
			}
		}else if(control == 'P'){
			cin >> alphabet;
			L.insert(t,alphabet);
		}
		
	}
	for(auto i : L) cout << i;
}