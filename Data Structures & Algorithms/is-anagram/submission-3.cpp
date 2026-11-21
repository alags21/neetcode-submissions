class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> smap, tmap;
        for (int i = 0; i<s.size(); i++) {
            if (smap.count(s[i])) {
                smap[s[i]] = smap[s[i]] + 1;
            } else {
                smap[s[i]] = 1;
            }
            if (tmap.count(t[i])) {
                tmap[t[i]] = tmap[t[i]] + 1;
            } else {
                tmap[t[i]] = 1;
            }
        }
        return (smap == tmap);
    }
};
