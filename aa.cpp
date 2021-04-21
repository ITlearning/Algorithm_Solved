#include <iostream>

using namespace std;

int board[64][64];

void dfs(int N, int x, int y){
    int ao=0;
    int az=0;
    if(N==1){
        cout<<board[x][y];
        return ;
    }
    for(int i=x;i<x+N;i++){
        for(int j=y;j<y+N;j++){
            if(board[i][j]==1){
                ao++;
            }
            else{
                az++;
            }
        }
    }
    if(ao==N*N){
        cout<<1;
    }
    else if(az==N*N){
        cout<<0;
    }
    else{
        cout<<"(";
        dfs(N/2,x,y);
        dfs(N/2,x,y+N/2);
        dfs(N/2,x+N/2,y);
        dfs(N/2,x+N/2,y+N/2);
        cout<<")";
    }

}

int main(){
    int N;
    string str;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>str;
        for(int j=0;j<N;j++){
            board[i][j]=str[j]-'0';
        }
    }
    dfs(N,0,0);
    return 0;
}