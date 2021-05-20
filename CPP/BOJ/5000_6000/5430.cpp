#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	string con;
	int T;
	
	cin >> T;
	string type_num;
	int num;
	string a;
	while(T--) {
		cin >> con;
		cin >> num;
		cin >> type_num;
		deque<int> dq;
			for(int i = 0; i < type_num.length(); i++) {
				if(type_num[i] == '[') {
					continue;
				} else if (type_num[i] >= '0' && type_num[i] <= '9') {
					a += type_num[i];
				} else if (type_num[i] == ',' || type_num[i] == ']') {
					if(!a.empty()) {
						dq.push_back(stoi(a));
						a.clear();
					}
				}
			}
		
		bool print = true;
		bool tmp = true;
		for(int i = 0; i < con.length(); i++) {
			if(con[i] == 'R') {
				if(tmp == true) {
					tmp = false;
				} else {
					tmp = true;
				}
			} else if (con[i] == 'D') {
				if(dq.empty()){
					print = false;
					cout << "error" << '\n';
					break;
				}
				if(tmp == false) {
					dq.pop_back();
				} else {
					dq.pop_front();
				}
			}
		}
		
		if(print) {
			cout << "[";
				if(tmp == false) {
				while(!dq.empty()) {
					cout << dq.back();
					dq.pop_back();
					if(!dq.empty()) {
						cout << ",";
					}
				}
				cout << "]\n";
			} else if (tmp == true) {
				while(!dq.empty()) {
					cout << dq.front();
					dq.pop_front();
					if(!dq.empty()){
						cout << ",";
					}
				}
				cout << "]\n";
			}
		}
	}
}