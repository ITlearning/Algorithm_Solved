#include <bits/stdc++.h>
using namespace std;
const int MX = 100;
int dat[MX];
int pre[MX], nxt[MX];
int unused = 1;

void insert(int addr, int num) {
	dat[unused] = num;
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


int main() {
	fill(pre, pre+MX, -1);
	fill(nxt, pre+MX, -1);
	int n, k;
	int size = 0;
	int cursor = 0;
	cin >> n >> k;
	for(int i = 1; i <= n; i++) {
		insert(size, i);
		size++;
	}
	cout << "<";
	while(size != 0) {
		for(int i = 0; i < k-1; i++) {
			cursor++;
			if(cursor == size) {
				cursor = 0;
			}
		}
		cout << dat[cursor] << ", ";
		erase(cursor);
		if(cursor == size) {
			cursor = 0;
		}
		cursor++;
		size--;
	}
	cout << dat[size] << ">";
}