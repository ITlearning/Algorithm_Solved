// 가운데 글자 가져오기
// 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    if(s.size() % 2 != 0) {
        int mid = s.size() / 2;
        answer = s[mid];
    } else {
        int mid = s.size() / 2;
        answer += s[mid - 1];
        answer += s[mid];
    }
    
    return answer;
}