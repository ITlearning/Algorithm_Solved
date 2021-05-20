#include <string>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    // 오른차순 정렬을 통해, 같은 위치에 있는 선수들을 비교한다.
    for(int i = 0; i < completion.size(); ++i) {
        if(participant[i] != completion[i]) {
            return participant[i];
        }
    }
    // 비교 후 만약 같은 자리에 다른 이름이 있는 선수일 경우 완주를 못한 선수이기때문에 출력을 해준다.
    return participant[participant.size()-1];
	// 그게 아니고 아얘 완주자에 없는 선수라면 마지막 선수를 출력해준다.
}