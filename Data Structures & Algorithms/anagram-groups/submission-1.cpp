class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // stores a frequency map, index in the vector
        vector<vector<string>> res;
        map<map<char, int>, int> str_mps;
        for (int i = 0; i < strs.size(); i++) {
            map<char,int> frq;
            for (int j = 0; j < strs[i].size(); j++) {
                frq[strs[i][j]]++;
            }
            if (str_mps.contains(frq)) {
                res[str_mps[frq]].push_back(strs[i]);
            } else {
                str_mps[frq] = res.size();
                res.push_back({strs[i]});
            }
        }
        return res;
    }
};
