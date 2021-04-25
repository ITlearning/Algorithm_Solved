#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n,m;
int board[10];
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
	
	for(int i = 0; i < n; i++) {
        if(!isused[i]) { // 아직 사용되지 않은 경우
            arr[k] = board[i];
            isused[i+1] = 1;
            func(k+1);
			for(int i = 0; i < n; i++) {
				isused[i] = 0;
			}
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
	
	for(int i = 0; i < n; i++) {
		cin >> board[i];
	}
	sort(board,board+n);
    func(0);
	
}
