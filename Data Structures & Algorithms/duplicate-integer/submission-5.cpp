class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> st;
        for (int num : nums) {
            if (st.contains(num)) {
                return true;
            } else {
                st.insert(num);
            }
        }
        return false;
    }
};