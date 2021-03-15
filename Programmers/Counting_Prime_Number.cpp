// 소수 찾기
// 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

// 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
// (1은 소수가 아닙니다.)


// 에라토스테네스의 체
// https://donggoolosori.github.io/2020/10/16/eratos/

#include <string>
#include <cmath>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int *prime = new int[n  + 1];
    for(int i = 2; i <= n; i++) {
        prime[i] = i;
    }
    
    for(int i = 2; i <= sqrt(n); i++) {
        if (prime[i] == 0) {
            continue;
        }
        for(int j = i * i; j <= n; j+= i)
            prime[j] = 0;
    }
    
    for(int i =2; i <= n; i++) {
        if(prime[i] != 0) {
            answer++;
        }
    }
    return answer;
}