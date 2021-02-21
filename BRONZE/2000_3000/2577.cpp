#include <iostream>
#include <string>
using namespace std;

int main() {
	char num;
	int size[10] = {0};
	int A,B,C;
	cin >> A >> B >> C;
	
	int total = A * B * C;
	
	while(total > 0) {
		size[total % 10]++;
		total /= 10;
	}
	
	for(int i = 0; i < 10; i++) {
		cout << size[i] << endl;
	}
}