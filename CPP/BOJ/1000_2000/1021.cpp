#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	int x;
	deque<int> dq;
	cin >> t >> x;
	for(int i = 1; i <= t; ++i) {
		dq.push_back(i);
	}
	int index;
	int num;
	int cnt = 0;
	while(x--){
		cin >> num;
		
		for(int i = 0; i < dq.size(); ++i) {
			if(dq[i] == num) {
				index = i;
				break;
			}
		}
		
		if(index < (dq.size()-index)) {
			while(1){
				if(dq.front() == num){
					dq.pop_front();
					break;
				}
				++cnt;
				dq.push_back(dq.front());
				dq.pop_front();
			}
		} else {
			while(1) {
				if(dq.front() == num) {
					dq.pop_front();
					break;
				}
				++cnt;
				dq.push_front(dq.back());
				dq.pop_back();
			}
		}
	}
	
	cout << cnt << endl;
}