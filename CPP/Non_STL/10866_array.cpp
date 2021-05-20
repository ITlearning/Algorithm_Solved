#include <bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int dat[2*MX+1];
int head = MX, tail = MX;

void push_front(int x){
	dat[--head] = x;
}

void push_back(int x){
  dat[tail++] = x;
}

int pop_front(){
	if(tail - head == 0) {
		return -1;
	}
	return dat[head++];
}

int pop_back(){
	if(tail - head == 0) {
		return -1;
	}
	return dat[--tail];
  
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
	
	int t;
	cin >> t;
	while(t--) {
		string c;
		cin >> c;
		if(c == "push_front") {
			int num;
			cin >> num;
			push_front(num);
		} else if(c == "push_back") {
			int num;
			cin >> num;
			push_back(num);
		} else if(c == "pop_front") {
			cout << pop_front() << '\n';
		} else if(c == "pop_back") {
			cout << pop_back() << '\n';
		} else if(c == "size") {
			cout << size() << '\n';
		} else if(c == "empty") {
			cout << empty() << '\n';
		} else if(c == "front") {
			cout << front() << '\n';
		} else if(c == "back") {
			cout << back() << '\n';
		}
	}
}