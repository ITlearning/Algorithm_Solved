#include <bits/stdc++.h>
using namespace std;

const int MX = 100005;
int A[MX];
int B[MX];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	for(int i = 0; i < N; i++) {
		cin >> A[i];
		B[A[i] - 1]++;
	}
	cin >> N;
	int tmp;
	for(int i = 0; i < N; i++) {
		cin >> tmp;
		if(B[tmp - 1] > 0) {
			cout << "1" << endl;
		} else {
			cout << "0" << endl;
		}
	}
}