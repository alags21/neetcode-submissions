class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> comps;
        // for every item, calculate the complement, and see if it has alreday been found in the list
        int comp;
        for (int i = 0; i < nums.size(); i++) {
            comp = target - nums[i];

            auto it = comps.find(comp);

            if (it != comps.end()) {
                return {min(i, comps[comp]), max(i, comps[comp])};
            }

            comps[nums[i]] = i;
        }

        return {};
    }
};
