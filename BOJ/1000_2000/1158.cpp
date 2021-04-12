#include <bits/stdc++.h>
using namespace std;


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, k;
	list<int> L;
	list<int>::iterator t;
	cin >> n >> k;
	
	for(int i = 1; i <= n; i++) {
		L.push_back(i);
	}
	cout << "<";
	t = L.begin();
	while(L.size() != 1) {
		for(int i = 0; i < k-1; i++) {
			t++;
			if(t == L.end()) {
				t = L.begin();
			}
		}
		cout << *t << ", ";
		t = L.erase(t);
		if(t == L.end()) {
			t = L.begin();
		}
	}
	cout << *t << ">";
}