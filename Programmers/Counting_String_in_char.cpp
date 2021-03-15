// 문자열 내 p와 y의 개수
/* 
 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
 s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
*/

// 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int a = 0;
    int b = 0;
    for(int i = 0; i < s.size(); i++) {
        if((s[i] == 'p' || s[i] == 'P')) {
            a++;
        }else if (s[i] == 'y' || s[i] == 'Y'){
            b++;
        }
    }
    
    if(a == b) {
        answer = true;
    }else if (a != b){
        answer = false;
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << a << ' ' << b << endl;

    return answer;
}