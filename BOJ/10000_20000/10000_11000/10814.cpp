#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool comp(pair<int,string> a, pair<int,string> b) {
	return a.first < b.first;
}

int main() {
	int n;
	vector<pair<int, string>> v;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		int num;
		string name;
		cin >> num >> name;
		v.push_back(pair<int,string>(num,name));
	}
	
	stable_sort(v.begin(),v.end(), comp);
	// 원래의 순서를 손상시키지 않으면서 정렬하는 것.
	vector<pair<int,string>>::iterator iter;
	for(iter = v.begin(); iter != v.end(); iter++) {
		cout << iter->first << ' ' << iter->second << '\n';
	}
}