#include <bits/stdc++.h>
using namespace std;

int main() {
    string text;
    getline(cin,text,'\n');
    //reverse(text.begin(),text.end());
    for(int i = text.size()-1; i >= 0; i--) {
        
        cout << text[i];
    }
    cout << endl;
}