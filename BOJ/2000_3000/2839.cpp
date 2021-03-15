#include <iostream>
using namespace std;

int main(void) {
    int kg;
    cin >> kg;

    for( int i=kg/5; i>=0 ;i--) {
        for(int j=0; (kg-5*i)/3 >= j ;j++){
            if(kg ==(i*5 + j*3)) {
                cout<<i+j;
                return 0;
            }
        }
    }
    cout << "-1";
    return 0;
}