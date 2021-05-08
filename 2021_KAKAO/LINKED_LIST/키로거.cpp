#include <bits/stdc++.h>
using namespace std;

int main() {
	int test_case;
	cin >> test_case;
	string text;
	for(int i = 0; i < test_case; i++) {
		list<char> L;
		list<char>::iterator t = L.begin();
		cin >> text;
		int text_len = text.size();
		for(int i = 0; i < text_len; i++) {
			if(text[i] == '<') {
				if(t != L.begin()) {
					t--;
				}
			} else if (text[i] == '>') {
				if(t != L.end()) {
					t++;
				}
			} else if (text[i] == '-') {
				if(t != L.begin()) {
					t--;
					t = L.erase(t);
				}
			} else {
				L.insert(t,text[i]);
			}
		}
		
		for(auto i : L) cout << i;
		cout << '\n';
	}
}