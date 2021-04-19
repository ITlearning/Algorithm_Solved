#include <iostream>
#include <vector>
using namespace std;

int *solution(int tmp[],vector<int> arr) {
    
    for(int i = 0; i < arr.size(); i++) {
        tmp[arr[i]-1]++;
    }

    return tmp;
}

int main() {
    vector<int> arr = {1,2,3,3,3,3,4,4};
    vector<int> v;
    int tmp[10] = {0};
    bool t = false;
    int *tm = solution(tmp,arr);

    cout << '[';
    for(int i = 0; i < 9; i++) {
        if(tm[i] >= 2) {
            t = true;
            cout << tm[i];
            
        }
    }

    if(!t) {
        cout << -1;
    }
    cout << ']';
}