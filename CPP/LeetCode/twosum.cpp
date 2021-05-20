class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        bool t = true;
        for(int i = 0; i < nums.size(); i++) {
            int tmp = target - nums[i];
            for(int j = i+1; j < nums.size(); j++) {
                if(tmp == nums[j] && t) {
                    v.push_back(i);
                    v.push_back(j);
                    t = false;
                    break;
                }
            }
        }
        return v;
    }
};