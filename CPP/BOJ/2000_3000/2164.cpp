#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	queue<int> q;
	int card;
	cin >> card;
	for(int i = 1; i <= card; i++) {
		q.push(i);
	}
	
	int size = q.size();
	while(size != 1) {
		q.front();
		q.pop();
		size--;
		int a = q.front();
		q.push(a);
		q.pop();
	}
	
	cout << q.front() << '\n';
}