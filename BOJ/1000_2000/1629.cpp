#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll recursion(ll a, ll b, ll m) {
	if(b == 1) return a % m;
	ll tmp = recursion(a,b/2,m);
	tmp = tmp * tmp % m;
	if(b%2 == 0) return tmp;
	return tmp * a % m;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	ll a,b,c;
	cin >> a >> b >> c;
	cout << recursion(a,b,c);
}