#include <iostream>
using namespace std;
int gradeM[6];
int gradeG[6];
int main() {
	int cnt = 0;
	int gender;
	int grade;
	int N;
	int max;
	cin >> N >> max;
	for(int i = 0; i < N; i++) {
		cin >> gender >> grade;
		if(gender == 0) {
			gradeG[grade - 1]++;
		} else if (gender == 1) {
			gradeM[grade - 1]++;
		}
	}
	for(int i = 0; i < 6; i++) {
		int m = gradeM[i] / max;
		int g = gradeG[i] / max;
		if((gradeM[i] % max) != 0) m++;
		if((gradeG[i] % max) != 0) g++;
		cnt += m + g;
	}
	cout << cnt;
}