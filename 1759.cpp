#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int n,m;
char board[50];
char arr[50];
int isused[50];

void func(int k,int index) {
    if(k == n) {
		 for(int i = 0; i < n; i++) {
            cout << arr[i];
        }
        cout << endl;
        return; // 리턴을 해서 바로 윗 단계로 올라감
	}
	int used[10000] = {0};
	for(int i = index; i < m; i++) {
		if(used[board[i] - 'a'] == 0){
			used[board[i] - 'a'] = 1;
			arr[k] = board[i];
			func(k+1, i+1);
		}
	}
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
	cin >> n >> m;
	
	for(int i = 0; i < m; i++) {
		cin >> board[i];
	}
	sort(board,board+m);
   	func(0,0);
	cout << endl;
    
	
}
