#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	double *p = new double[n];
	int max = 0;
	double newResult = 0;
	for(int i = 0; i < n; i++) {
		cin >> p[i];
		if(p[i] > max){
			max = p[i];
		}
		newResult += p[i];
	}
	
	newResult = (newResult / max * 100) / n;
	cout << fixed;
	cout.precision(6);
	cout << newResult << '\n';
}