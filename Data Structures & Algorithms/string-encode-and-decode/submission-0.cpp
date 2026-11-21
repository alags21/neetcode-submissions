class Solution {
public:

    string encode(vector<string>& strs) {
        // could just smoosh all the strings together wit
        string enc = "";
        for (const string str : strs) {
            string len = to_string(str.size());
            enc += len + "#" + str;
        }
        return enc;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        string currlen;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '#') {
                int len = stoi(currlen);
                ans.push_back(s.substr(i+1, len));
                i += len;
                currlen = "";
            } else {
                currlen += s[i];
            }
        }
        return ans;
    }
};
