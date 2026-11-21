class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // iterating over nums
        // sorting won't work since its O(nlogn)
        // we can create a hashmap for O(1) searching
        // the key is the number in the array
        // we need a way to store the current sequences - vector of sequences?
        // for each element we can search if the adjacent ints are keys in the hashtable
        // if they are found, then we have found two consecutive elements

        unordered_set<int> numset;
        
        for (int n: nums) {
            numset.insert(n);
        }

        int ans = 0;
        int currNum = 0;
        int currLen = 0;
        for (int num : numset) {
            if (!numset.contains(num-1)) {
                currNum = num;
                currLen = 0;
                while (true) {
                    currLen++;
                    currNum = currNum+1;
                    if (!numset.contains(currNum)) {
                        ans = max(ans, currLen);
                        break;
                        }
                    }
                }
            }
        return ans;
        }

};
