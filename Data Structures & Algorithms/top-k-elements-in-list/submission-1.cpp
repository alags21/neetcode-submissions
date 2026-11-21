class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int i=0; i < nums.size(); i++) {
            freq[nums[i]]++;
        }

        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [ num, fre ] : freq ) {
            buckets[fre].push_back(num);
        }

        vector<int> ans;
        for (int j=nums.size(); ans.size() < k && j >= 0; j--) {
            for (int o : buckets[j]) {
                ans.push_back(o);
                if (ans.size() == k) {
                    break;
                }
            }
        }

        return ans;
    }
};
