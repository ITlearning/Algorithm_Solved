#include <bits/stdc++.h>
using namespace std;
#define MX 2000001
#define endl '\n'
int freq[MX];
int n;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int m;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int a;
        cin >> a;
        freq[a + 1000000]++;
    }
    int a = 1;
    for(int i = 0; i <= 2000000; i++) {
        while(freq[i]--) {
            cout << i-1000000 << '\n';
        }
    }
}
