#include <bits/stdc++.h>
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	vector<int> v(n);
	for(int i = 1; i <= n; i++)
		v[i-1] = i;
	do {
		for(int i = 0; i < n; i++) {
			cout << v[i] << ' ';
		}
		cout << '\n';
	} while(next_permutation(v.begin(), v.end()));
}