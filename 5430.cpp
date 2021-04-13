#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	deque<int> dq;
	string control;
	int T;
	int size;
	cin >> T;
	while(T--) {
		cin >> control;
		cin >> size;
		for(int i = 0; i < size; i++) {
			int num;
			cin >> num;
			dq.push_back(num);
		}
		int tmp = 0;
		int orisize = size;
		for(int i = 0; i < control.size(); i++) {
			if(control[i] == 'R') {
				tmp = 0;
				size = orisize;
				while(size != tmp) {
					size = size - 1;
					int a = dq[tmp];
					dq[tmp] = dq[size];
					dq[size] = a;
					tmp++;
					
				}
			} else if(control[i] == 'D') {
				if(dq.empty()) {
				cout << "error";
				break;
				}
				dq.pop_front();
			}
		}
		cout << "[";
		for(int i = 0; i < dq.size(); i++) {
			cout << dq[i] << ", ";
		}
		cout << "]";
		dq.clear();
		cout << '\n';
	}
	
	
}