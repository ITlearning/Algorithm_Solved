#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
int n,m;
int arr[10];
int isused[10];

void func(int k) {
    if(k == m) {
        for(int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        cout << endl;
        return; // 리턴을 해서 바로 윗 단계로 올라감
    }

    for(int i = 1; i <= n; i++) {
        if(!isused[i]) { // 아직 사용되지 않은 경우
            arr[k] = i;
            isused[i] = 1;
            func(k+1);
            isused[i] = 0;  // 모두 다 돌고 자기 자신의 수는 사용한게 아니니 false로 만든다.
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    func(0);
}