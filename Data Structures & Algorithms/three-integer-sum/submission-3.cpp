class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // sort first
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;

        for (int i = 0; i< nums.size()-2; i++) {
            
            if (i != 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int j = i + 1;
            int k = nums.size() - 1;
            int comp = 0 - nums[i];

            while (j < k) {
                int currsum = nums[k] + nums[j];
                if (currsum == comp) {
                    ans.push_back({nums[i], nums[j], nums[k]});
                    while (j < nums.size() - 1 && nums[j+1] == nums[j] && j < k) j++;
                    j++;
                    while (k > 0 && nums[k-1] == nums[k] && j < k) k--;
                    k--;
                } else if (currsum < comp) {
                    while (j < nums.size() - 1 && nums[j+1] == nums[j] && j < k) j++;
                    j++;
                } else {
                    while (k > 0 && nums[k-1] == nums[k] && j < k) k--;
                    k--;
                }
            }
        }
        return ans;
    }
};
