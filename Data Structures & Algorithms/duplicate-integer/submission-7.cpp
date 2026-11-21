class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> found;
        for (int n : nums) {
            if (found.contains(n)) {
                return true;
            } else {
                found.emplace(n);
            }
        }
        return false;
    }
};