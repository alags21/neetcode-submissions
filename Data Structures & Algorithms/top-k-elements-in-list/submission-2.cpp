class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // we should use bucket sort for this since its sorting based on frequency and we want
        // fast access to the last couple elements in the list

        // first build a character frequency map
        unordered_map<int, int> frqs;
        for (int i : nums) {
            frqs[i]++;
        }

        // now, make an array of buckets where index = frequency
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [num, frq] : frqs) {
            buckets[frq].push_back(num);
        }

        // starting from the last index, pop elements until ans array = k size or end reached
        vector<int> ans;
        for (int j=nums.size(); ans.size() < k && j >=0; j--) {
            for (int n : buckets[j]) {
                ans.push_back(n);
                if (ans.size() == k) {
                    break;
                }
            }
        }

        return ans;

    }
};
