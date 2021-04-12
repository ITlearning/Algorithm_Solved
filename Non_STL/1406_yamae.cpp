#include <bits/stdc++.h>
using namespace std;

const int MX = 1000005;
char dat[MX];
int pre[MX], nxt[MX];
int unused = 1;

void insert(int addr, char text) {
	dat[unused] = text;
	pre[unused] = addr;
	nxt[unused] = nxt[addr];
	if(nxt[addr] != -1) pre[nxt[addr]] = unused;
	nxt[addr] = unused;
	unused++;
}

void erase(int addr) {
	nxt[pre[addr]] = nxt[addr];
	if(nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
}

void traverse() {
	int cur = nxt[0];
	while(cur != -1) {
		cout << dat[cur];
		cur = nxt[cur];
	}
}

int main() {
	ios::sync_with_stdio(0);
  	cin.tie(0);
	fill(pre, pre+MX, -1);
	fill(nxt, nxt+MX, -1);
	string text;
	char alpha;
	cin >> text;
	int cursor = 0;
	for(auto c : text) {
		insert(cursor, c);
		cursor++;
	}
	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		char cas;
		cin >> cas;
		if (cas == 'L'){
			if(pre[cursor] != -1) {
				cursor = pre[cursor];
			}
		} else if (cas == 'D') {
			if(nxt[cursor] != -1) {
				cursor = nxt[cursor];
			}
		} else if (cas == 'B') {
			if(cursor != 0) {
				erase(cursor);
				cursor = pre[cursor];
			}
		} else if(cas == 'P') {
			cin >> alpha;
			insert(cursor, alpha);
			cursor = nxt[cursor];
		}
	}
	traverse();
}