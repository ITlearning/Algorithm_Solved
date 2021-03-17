#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool comp(int a, int b) {
	if(a == b) return a < b;
	else return a < b;
}


int main() {
	int n;
	int text;
	vector<int> v;
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> text;
		// 입력할때 이게 있는지 없는지 확인 거치는것. 이게 핵심
		if(find(v.begin(),v.end(), text) == v.end()) 
			v.push_back(text);
	}
	
	sort(v.begin(), v.end(), comp);
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << ' ';
	}
}