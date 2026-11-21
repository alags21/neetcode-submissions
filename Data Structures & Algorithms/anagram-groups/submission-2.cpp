class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // We want to create a map of strings and their sorted counterparts
        unordered_map<string, vector<string>> str_maps;
        for (const string& str: strs) {
            // sort the string
            string sorted = str;
            sort(sorted.begin(), sorted.end());
            str_maps[sorted].push_back(str);
        }

        vector<vector<string>> ans;
        for (auto& [str_, grp] : str_maps) {
            ans.push_back(grp);
        }

        return ans;
    }

};
