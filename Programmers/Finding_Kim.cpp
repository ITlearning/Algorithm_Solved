// 서울에서 김서방 찾기
// String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
// seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    for(int i = 0; i < seoul.size(); i++) {
        if(seoul[i] == "Kim") {
            answer = "源??꽌諛⑹?? " + to_string(i) + "?뿉 ?엳?떎";
        }
    }
    return answer;
}