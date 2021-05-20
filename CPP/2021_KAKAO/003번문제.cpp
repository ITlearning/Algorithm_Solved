#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int dist[1000002];
string solution(int n, int k, vector<string> cmd) {
    string answer = "";
    vector<int> trash;
    
    memset(dist,0, sizeof(dist));
    int cur = k;
    int max = n;
   for(int i = 0; i < cmd.size(); i++) {
        if(cmd[i][0] == 'D') {
            string num;
            for(int j = 0; j < cmd[i].size(); j++) {
                if(cmd[i][j] >= 48 && cmd[i][j] <= 57)
                num += cmd[i][j];
            }
            if(cur + stoi(num) != max && cur + stoi(num) != 0) {
                cur += stoi(num);
                num = "";
            } 
        } else if (cmd[i][0] == 'U') {
            string num;
            for(int j = 0; j < cmd[i].size(); j++) {
                if(cmd[i][j] >= 48 && cmd[i][j] <= 57)
                num += cmd[i][j];
            }
            if((cur - stoi(num)) != 0 && (cur - stoi(num)) != max) {
                cur -= stoi(num);
                num = "";
            }
        } else if (cmd[i][0] == 'C') {
            if(max != 0) {
                if(cur == max) {
                trash.push_back(cur);
                dist[cur] = 1;
                max -= 1;
                } else {
                trash.push_back(cur);
                dist[cur] = 1;
                max -= 1;
                }
            }
        } else if (cmd[i][0] == 'Z') {
            if(!trash.empty()) {
                int t = trash.back();
                trash.pop_back();
                dist[t] = 0;
                max += 1;
            }
        }
    }
    
   for(int i = 0; i < n; i++) {
        if(dist[i] == 1) {
            answer += "X";
        } else {
            answer += "O";
        }
    }
    return answer;
}