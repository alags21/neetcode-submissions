class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;
        unordered_map<char, int> currStr;
        currStr[s[0]] = 0;
        int i = 0;
        int j = 1;
        int maxLen = 1;
        int currLen = 1;


        while (j < s.size()) {
            if (currStr.contains(s[j])) {
                while (i<=currStr[s[j]]) {
                    currStr.erase(s[i]);
                    i++;
                    currLen--;
                }
                currStr[s[j]] = j;
                currLen++;
                j++;

                continue;
            } else {
                currStr[s[j]] = j;
                currLen++;
                j++;
            }
            maxLen = max(maxLen, currLen);
        }

        return maxLen;
    }
};
