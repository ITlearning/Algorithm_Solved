class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> v;
        int tmp = 0;
        for(int i = 0; i < nums.size(); i++){
            tmp += nums[i];
            v.push_back(tmp);
        }
        return v;
    }
};