// 작성완료

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	vector<int> v;
	int len;
	cin >> len;
	
	for(int i = 0; i < len; i++) {
		string cnt;
	cin >> cnt;
	if (cnt == "push") {
		int num;
		cin >> num;
		v.push_back(num);
	}
	else if (cnt == "pop") {
		if(v.empty()) {
			cout << "-1" << endl;
		} else {
			cout << v.back() << endl;
			v.pop_back();
		}
	}
	else if (cnt == "size") {
		cout << v.size() << endl;
	}
	else if (cnt == "empty") {
		cout << v.empty() << endl;
	}
	else if (cnt == "top") {
		if(v.empty()) {
			cout << "-1" << endl;
		}
		else {
			cout << v.back() << endl;
		}
	}
	else {
		cout << "ERROR" << endl;
		}
	}
	
}