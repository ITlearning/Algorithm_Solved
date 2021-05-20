#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n,m;
int board[10];
int arr[10];
int isused[10];

void func(int k,int index) {
    if(k == m) {
		 for(int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        cout << endl;
        return; // 리턴을 해서 바로 윗 단계로 올라감
	}
	int used[10000] = {0};
	for(int i = index; i < n; i++) {
		if(used[board[i]] == 0){
			used[board[i]] = 1;
			arr[k] = board[i];
			func(k+1, i+1);
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
    func(0,0);
	
}
