#include <vector>
#include <queue>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
#define X first
#define Y second
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
bool dist[100][100];
int dfs(int i , int j, int m, int n, vector<vector<int>> board) {
    int tmp = board[i][j];
    queue<pair<int,int>> Q;
    int cnt = 1;
    Q.push({i,j});
    dist[i][j] = true;
    while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        for(int i = 0; i < 4; i++){
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];
            if(nx>=0 && ny>=0 && nx < m && ny < n){
                if (board[nx][ny] == tmp && dist[nx][ny] == false) {
                dist[nx][ny] = true;
                Q.push({nx,ny});
                cnt++;
                } 
            } 
        }
    }
    return cnt;
    
}



// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            dist[i][j] = false;
        }
    }
    
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    vector<int> s;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (picture[i][j] != 0 && dist[i][j] == false) {
                int C = dfs(i,j,m,n, picture);
                if(C > max_size_of_one_area) max_size_of_one_area = C;
                number_of_area++;
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}