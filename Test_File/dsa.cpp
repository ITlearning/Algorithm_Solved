#include <bits/stdc++.h>
using namespace std;

const int MX = 5001;
int dat[MX];
int pre[MX], nxt[MX];
int unused = 1;

void insert(int addr, int num) {
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

int main() {
	
}