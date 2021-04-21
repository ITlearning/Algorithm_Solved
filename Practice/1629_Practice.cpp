#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll func(ll a,ll b, ll c) {
    if(b == 1) return a % c; // 제곱수가 1일 경우에 그냥 a를 c로 나눈 나머지를 출력한다.
    ll tmp = func(a, b /2, c); // 그게 아닐경우에 원시적인 방법으로 구하면 크기가 너무 커져서, 제곱수를 반으로 나눈 뒤 구해본다.
    tmp = tmp*tmp % c;  // 반으로 나눈 제곱수를 제곱하여 나머지를 구한다.
    if(b%2 == 0) return tmp;  // 만약 제곱수가 짝수일 경우, 그냥 tmp를 return 한다.
    return tmp * a % c;        // 만약 홀수일 경우엔 a를 한 번 더 곱해야 한다.
}




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll a,b,c;
    cin >> a >> b >> c;
    cout << func(a,b,c);
}