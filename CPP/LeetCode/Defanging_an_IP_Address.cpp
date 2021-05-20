class Solution {
public:
    string defangIPaddr(string address) {
        string tmp = "";
        for(int i = 0; i < address.size(); i++) {
            if(address[i] == '.') {
                tmp += '[';
                tmp += address[i];
                tmp += ']';
            }else {
                tmp += address[i];
            }
            
        }
         return tmp;
    }
};