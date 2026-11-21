class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size()-1;
        while (i < j) {
            char c1 = tolower(s[i]);
            char c2 = tolower(s[j]);
            while ((!isalnum(c1)) & (i < j)) {
                i++;
                c1 = tolower(s[i]);
            }
            while ((!isalnum(c2)) & (i < j)) {
                j--;
                c2 = tolower(s[j]);
            }
            if (c1 != c2) {
                return false;
            }
            j--;
            i++;
        }
        return true;
    }
};
