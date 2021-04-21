#include <bits/stdc++.h>
using namespace std;

// 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력하는 함수
void func(int a, int b, int n) { 
    if(n == 1) {
        cout << a << ' ' << b << '\n';
        return;
    }
    func(a,6-a-b, n-1);             // n-1 개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다.
    cout << a << ' ' << b << '\n';  // n번 원판을 기둥 a에서 기둥 b로 옮긴다.
    func(6-a-b, b, n-1);            // n-1 개의 원판을 기둥 6-a-b 에서 기둥 b로 옮긴다.
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    cout << (1<<t) - 1 << '\n'; // 2^t - 1 . left shift 라는 비트 연산자
    func(1,3,t);
}