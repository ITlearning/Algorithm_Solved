// [카카오 인턴] 키패드 누르기

/* 정해진 패턴대로 누르기 */

#include <string>
#include <vector>
#define X first
#define Y second
using namespace std;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
vector<pair<int,int>> leftHand;
vector<pair<int,int>> rightHand;
int phone[4][3] = { {1,2,3},
                    {4,5,6},
                    {7,8,9},
                    {10,0,11} };

string func(int n, string h) {
    if(n == 1 || n == 4 || n == 7) {
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 3; j++) {
                if(phone[i][j] == n) {
                    if(!leftHand.empty()) {
                        leftHand.pop_back();
                        leftHand.push_back({i,j});
                    } else {
                        leftHand.push_back({i,j});
                    }
                    return "L";
                }
            }
        }
    } else if (n == 3 || n == 6 || n == 9) {
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 3; j++) {
                if(phone[i][j] == n) {
                    if(!rightHand.empty()) {
                        rightHand.pop_back();
                        rightHand.push_back({i,j});
                    } else {
                        rightHand.push_back({i,j});
                    }
                    return "R";
                }
            }
        }
    } else {
        auto lhand = leftHand.front();
        auto rhand = rightHand.front();
        vector<pair<int,int>> answer;
        
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 3; j++) {
                if(phone[i][j] == n) {
                    if(!answer.empty()) {
                        answer.pop_back();
                        answer.push_back({i,j});
                    } else {
                        answer.push_back({i,j});
                    }
                }
            }
        }
        auto an = answer.front();
        
        int l = abs(an.X - lhand.X) + abs(an.Y - lhand.Y);
        int r = abs(an.X - rhand.X) + abs(an.Y - rhand.Y);
        
        if(l == r){
            if(h == "left") {
                leftHand.pop_back();
                leftHand.push_back({an.X,an.Y});
                return "L";
            } else if(h == "right") {
                rightHand.pop_back();
                rightHand.push_back({an.X,an.Y});
                return "R";
            }
        } else {
            if(l < r) {
                leftHand.pop_back();
                leftHand.push_back({an.X,an.Y});
                return "L";
            } else {
                rightHand.pop_back();
                rightHand.push_back({an.X,an.Y});
                return "R";
            }
        }
    }
}
string solution(vector<int> numbers, string hand) {
    string answer = "";
    leftHand.push_back({3,0});
    rightHand.push_back({3,2});
    for(int i = 0; i < numbers.size(); i++) {
        answer += func(numbers[i], hand);
    }
    return answer;
}