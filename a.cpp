#include <bits/stdc++.h>
using namespace std;

string line;
stack<char> S;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int ansNum = 1; // 출력을 자세히 보면 `1. 정답`의 형태. 
    while (true)
    {
        cin >> line;
        int ans = 0;
        for (int i = 0; i < line.size(); i++)
        {
            char c = line[i];
            if (c == '{')
            {
                S.push(c);
            }
            else if (c == '}')
            {
                if (S.empty() || S.top() != '{')
                {
                    S.push(c);
                }
                else // S.top() == '{'
                {
                    S.pop();
                }
            }
            else // c == '-'
            {
                return 0;
            }
        }
        while (!S.empty())
        {
            char t = S.top();
            S.pop();
            if (S.top() != t)
            {
                ans += 2;
            }
            else // S.top() == t. '{' == '{'
            {
                ans += 1;
            }
            S.pop();
        }
        cout << ansNum++ << ". " << ans << '\n';
    }
}