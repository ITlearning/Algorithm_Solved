#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	vector<int> v;
	int n;
	cin >> n;
	for(int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if(find(v.begin(), v.end(), num) == v.end())
			v.push_back(num);
	}
	
	sort(v.rbegin(), v.rend());
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << endl;
	}
}