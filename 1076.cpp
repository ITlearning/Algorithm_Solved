#include <bits/stdc++.h>
using namespace std;

int main() {
	map<string, int> m;
	m.insert(pair<string, int>("black", 0));
	m.insert(pair<string, int>("brown", 1));
	m.insert(pair<string, int>("red", 2));
	m.insert(pair<string, int>("orenge", 3));
	m.insert(pair<string, int>("yellow", 4));
	m.insert(pair<string, int>("green", 5));
	m.insert(pair<string, int>("blue", 6));
	m.insert(pair<string, int>("violet", 7));
	m.insert(pair<string, int>("grey", 8));
	m.insert(pair<string, int>("white", 9));
	int a,b;
	int count = 0;
	int total = 0;
	long long gop[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };
	string color;
	for(int i = 0; i < 3;i++) {
		cin >> color;
		count++;
		if(m.find(color) != m.end()) {
			a = m.find(color)->second;
			cout << stotal[i] << endl;
		}
		
	}
}