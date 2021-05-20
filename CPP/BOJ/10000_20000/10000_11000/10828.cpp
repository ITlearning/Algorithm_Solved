#include <bits/stdc++.h>
using namespace std;

const int MX = 100005;
int dat[MX];
int pos = 0;

void push(int x) {
	if(pos <= 0) {
		pos = 0;
		dat[pos++] = x;
	}else {
		dat[pos++] = x;
	}
	
}

int pop() {
	if(pos <= 0) {
		return -1;
	}
	
	return dat[--pos];
}

int top() {
	if(pos <= 0) {
		return -1;
	}
	return dat[pos - 1];
	
}

int empty() {
	if(pos <= 0) {
		return 1;
	} else{
		return 0;
	}
}

void size() {
	cout << pos << '\n';
}

int main() {
	int T;
	string a;
	cin >> T;
	int num;
	for(int i = 0; i < T; i++) {
		cin >> a;
		if(a == "top") {
			cout << top() << '\n';
		}  else if (a == "empty") {
			cout << empty() << '\n';
		} else if (a == "size"){
			size();
		} else if (a == "push"){
			cin >> num;
			push(num);
		} else if (a == "pop") {
			cout << pop() << '\n';
		}
		
	}
}