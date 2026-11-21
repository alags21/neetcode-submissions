class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // iterate through starting from index 1.
        // for each item, keep a prefix array that holds the result from the product of all previous numbers
        // then keep a suffix array that holds the result from the product all future numbers

        // building prefix array
        vector<int> prefix(nums.size());
        // nothing to the left of 0th index
        prefix[0] = 1;
        for (int i = 1; i < nums.size(); i++) {
            prefix[i] = prefix[i-1] * nums[i-1];
        }

        vector<int> suffix(nums.size());
        // nothing to right of last index
        suffix[nums.size()-1] = 1;
        for (int j = nums.size() - 2; j >= 0; j--) {
            suffix[j] = suffix[j+1] * nums[j+1];
        }

        vector<int> output;
        // multiply prefix and suffix for each index to get ans
        for (int k=0; k < nums.size(); k++) {
            output.push_back(prefix[k] * suffix[k]);
        }
        return output;
    }
};
