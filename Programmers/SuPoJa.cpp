//프로그래머스 수포자 - 모의고사

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int mf1[5] = {1,2,3,4,5};
    int mf2[8] = {2,1,2,3,2,4,2,5};
    int mf3[10] = {3,3,1,1,2,2,4,4,5,5};
    int box[3] = {};
    
    // answers를 다 돌면서 맞을 경우 1 늘리기
    for(int i = 0; i < answers.size(); i++) {
        if(mf1[i%5] == answers[i]) {
            box[0]++;
        }
        if(mf2[i%8] == answers[i]) {
            box[1]++;
        }
        if(mf3[i%10] == answers[i]) {
            box[2]++;
        }
    }
    

    // 가장 큰 수가 어떤건지 걸러내기
    // 만일 가장 큰 수와 같은 수가 존재할 경우에는 일단 answer에 추가
    int mx = 0;
    for(int i = 1; i < 3; i++) {
        if(box[mx] < box[i]) {
            mx = i;
        } else if(box[mx] == box[i]) {
            answer.push_back(i+1);
        }
    }

    // 가장 큰 수가 하나일 경우에는 하나만 추가
    answer.push_back(mx+1);
    // 일단 넣어놨던 숫자들이 오름차순이 되도록 sort() 돌리기
    sort(answer.begin(),answer.end());
    return answer;
}