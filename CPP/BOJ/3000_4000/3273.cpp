#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	int cnt = 0;
	cin >> t;
	int *p = new int [t];
	for(int i = 0; i < t; i++) {
		cin >> p[i];
	}
	
	sort(p, p+t);
	int num;
	cin >> num;
	int start = 0;
	int end = t - 1;
	while(start < end) {
		if(p[start] + p[end] == num) {
			cnt++;
			start++;
			end--;
		} else if (p[start] + p[end] > num) {
			end--;
		} else if (p[start] + p[end] < num) {
			start++;
		}
	}
	delete p;
	cout << cnt;
}