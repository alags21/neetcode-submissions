class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> schars;
        unordered_map<char, int> tchars;

        if (s.size() != t.size()) {
            return false;
        }

        for (int i = 0; i < s.size(); i++) {
            schars[s[i]] += 1;
            tchars[t[i]] += 1;
        }

        return tchars==schars;
    }
};
