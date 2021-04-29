//프로그래머스 수포자 - 모의고사

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int mf1[5] = {1,2,3,4,5};
    int mf2[8] = {2,1,2,3,2,4,2,5};
    int mf3[10] = {3,3,1,1,2,2,4,4,5,5};
    int box[3] = {};
    for(int i = 0; i < answers.size(); i++) {
        if(mf1[i%5] == answers[i]) {
            box[0]++;
        }
    }
    
    for(int i = 0; i < answers.size(); i++) {
        if(mf2[i%8] == answers[i]) {
            box[1]++;
        }
    }
    
    for(int i = 0; i < answers.size(); i++) {
        if(mf3[i%10] == answers[i]) {
            box[2]++;
        }
    }
    
   if(box[0] == box[1] && box[0] == box[2]) {
        for(int i = 1; i<= 3; i++) {
            answer.push_back(i);
        }
    } else {
       int a = 0;
       int m = box[0];
       for(int i = 1; i < 3; i++) {
           if(m <= box[i]) {
               m = box[i];
               a = i;
               answer.push_back(i+1);
            } else if (m < box[i]){
               a = i;
               m = box[i];
           }
      }
       answer.push_back(a+1);
   }
    
        
   // answer.push_back(box[0]);
    //answer.push_back(box[1]);
    //answer.push_back(box[2]);
    return answer;
}