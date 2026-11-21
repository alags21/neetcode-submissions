class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numset;
        for (int num : nums) {
            if (!numset.contains(num)) {
                numset.insert(num);
            } else {
                return true;
            }
        }
        return false;
    }
};