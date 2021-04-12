#include <bits/stdc++.h>
using namespace std;

const int MX = 20000001;
int dat[MX];
int head = 0, tail = 0;

void push(int x){
	if(tail <= 0) {
		tail = 0;
		dat[tail++] = x;
	} else {
		dat[tail++] = x;
	}
	
}

int pop(){
	if(tail - head == 0) {
		return -1;
	}
	
	return dat[head++];
}

int front(){
	if(tail - head == 0) {
		return -1;
	}
	return dat[head];
}

int back(){
	if(tail - head == 0) {
		return -1;
	}
	
	return dat[tail - 1];
}

int size() {
	return tail - head;
}

int empty() {
	if(tail - head == 0) {
		return 1;
	}
	return 0;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int T;
	string con;
	cin >> T;
	while(T--) {
		cin >> con;
		if(con == "push") {
			int num;
			cin >> num;
			push(num);
		} else if(con == "pop") {
			cout << pop() << '\n';
		} else if(con == "size") {
			cout << size() << '\n';
		} else if(con == "empty") {
			cout << empty() << '\n';
		} else if(con == "front") {
			cout << front() << '\n';
		} else if(con == "back") {
			cout << back() << '\n';
		}
	}
}