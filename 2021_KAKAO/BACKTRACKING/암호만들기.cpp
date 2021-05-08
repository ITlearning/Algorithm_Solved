#include <bits/stdc++.h>
using namespace std;

int n,m;
char arr[20];


void func(int pos, string str, int jaem,int moem) {
	if(str.size() == n) {
		if(jaem < 2 || moem < 1) // 조건인 자음 2개 이상 모음 1개 이상 아니면 그냥 올라가기
			return;
		cout << str << endl; // 맞으면 출력
	}
	
	for(int i = pos; i < m; i++) {
		if(arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u')
			func(i+1, str+arr[i], jaem, moem+1);
		else
			func(i+1, str+arr[i], jaem+1, moem);
	}
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n >> m;
	
	for(int i = 0; i < m; i++) {
		cin >> arr[i];
	}
	
	sort(arr,arr+m);
	
	func(0, "", 0, 0);
}