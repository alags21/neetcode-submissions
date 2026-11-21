class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> cmps;
        for (int i=0; i<nums.size(); i++) {
            int cmp = target - nums[i];
            if (cmps.contains(cmp)) {
                return {cmps[cmp], i};
            } else {
                cmps[nums[i]] = i;
            }
        }
        return {0,0};
    }
};
