class Solution {
public:
    bool isAnagram(string s, string t) {
        // build a character map of both strings for frequency
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> s_frqs;
        unordered_map<char, int> t_frqs;
        for (int i=0; i < s.size(); i++) {
            s_frqs[s[i]]++;
            t_frqs[t[i]]++;
        }
        return (s_frqs==t_frqs);
    }
};
