#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 비교 함수
	// 외부의 정의된 비교함수(Comparison function)를 sort 함수에 콜백 함수 형태로 줄 수도 있다.
	// 예를 들어 함수 comp는 문자열을 먼저 길이순으로, 그리고 그다음에는 알파벳순으로 정렬한다.
	
bool comp(string a, string b) {
	if(a.size() == b.size()) return a < b;
	else return a.size() < b.size();
}


int main() {
	int n;
	string text;
	vector<string> v;
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> text;
		// 입력할때 이게 있는지 없는지 확인 거치는것. 이게 핵심
		if(find(v.begin(),v.end(), text) == v.end()) 
			v.push_back(text);
	}
	
	sort(v.begin(), v.end(), comp);
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << '\n';
	}
}