#include <iostream>

using namespace std;

int main() {
	int size;
	char num;
	int total = 0;
	cin >> size;
	
	for(int i = 0; i < size; i++) {
		cin >> num;
		total += (num - '0');
	}
	
	cout << total << '\n';
}