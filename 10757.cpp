#include <iostream>
#include <string>
using namespace std;

int main() {
	string sa,sb;
	int a,b;
	cin >> sa >> sb;
	if(sa.length() > sb.length()) {
		int tmp[sb.length()];
		for(int i = 0; i < sa.length(); i++) {
		a = sa[i] - '0';
		b = sb[i] - '0';
		tmp[i] = a + b;
		if(i != 0) {
			if(tmp[i] > 10) {
				tmp[i-1] += tmp[i] / 10;
				tmp[i] = tmp[i] % 10;
			} else if (tmp[i] == 10) {
				tmp[i-1] += 1;
				tmp[i] = tmp[i] % 10;
			}
		}
		
		}
		for (int i = 0; i < sa.length(); i++) {
		cout << tmp[i];
		}	
	}else if (sa.length() < sb.length()){
		int tmp[sa.length()];
		for(int i = 0; i < sb.length() - 1; i++) {
		a = sa[i] - '0';
		b = sb[i] - '0';
		tmp[i] = a + b;
		if(i != 0) {
			if(tmp[i] > 10) {
				tmp[i-1] += tmp[i] / 10;
				tmp[i] = tmp[i] % 10;
			} else if (tmp[i] == 10) {
				tmp[i-1] += 1;
				tmp[i] = tmp[i] % 10;
			}
		}
		
		}
		
		for (int i = 0; i < sb.length(); i++) {
		cout << tmp[i];
		}	
	} else {
		int tmp[sb.length()];
		for(int i = 0; i < sb.length(); i++) {
		a = sa[i] - '0';
		b = sb[i] - '0';
		tmp[i] = a + b;
		if(i != 0) {
			if(tmp[i] > 10) {
				tmp[i-1] += tmp[i] / 10;
				tmp[i] = tmp[i] % 10;
			} else if (tmp[i] == 10) {
				tmp[i-1] += 1;
				tmp[i] = tmp[i] % 10;
			}
		}
		
		}
		for (int i = 0; i < sb.length(); i++) {
		cout << tmp[i];
		}	
	}

	
}