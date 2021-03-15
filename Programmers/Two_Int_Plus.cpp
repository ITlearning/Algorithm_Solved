// 두 정수 사이의 합
// 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
// 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    vector<long long> v;
  
    
    if(a<b) {
         v.push_back(a);
        while(a < b) {
        a++;
        v.push_back(a);
        }
        for(int i = 0; i < v.size(); i++) {
            answer += v[i];
        } 
    } else {
        v.push_back(b);
        while(a > b) {
            b++;
            v.push_back(b);
        }
        for(int i = 0; i < v.size(); i++) {
            answer += v[i];
        }
    }
   
    return answer;
}