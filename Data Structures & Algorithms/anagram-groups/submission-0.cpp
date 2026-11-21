class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Compute map for char
        // Check if list of maps contains curr map
        // if so, add str to that list

        vector<vector<string>> result;
        map<map<char, int>, int> mps;
        for (int i = 0; i<strs.size(); i++) {
            string s = strs[i];
            map<char, int> s_map;
            for (int j = 0; j < s.length(); j++) {
                s_map[s[j]]++;
            }
            if (mps.contains(s_map)) {
                result[mps[s_map]].push_back(s);
            } else {
                mps[s_map] = result.size();
                result.push_back({s});
            }
        }
        return result;
    }
};
