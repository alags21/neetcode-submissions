class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // need 3 unordered set vectors for row, col, box

        vector<unordered_set<int>> rows(9);
        vector<unordered_set<int>> cols(9);
        vector<unordered_set<int>> boxes(9);

        // outer loop for rows
        int b = 0;
        for (int r=0; r < 9; r++) {
            for (int c=0; c < 9; c++) {
                // now we have cooridnate r, c
                // need box coorindate
                // 0-2 0-2 = 0
                // 0-2 3-5 = 1
                // 0-2 6-8 = 2
                // 3-5 0-2 = 4
                b = 3*(r/3) + (c/3);
                char dig = board[r][c];
                if (dig == '.') continue;
                if (rows[r].contains(dig) || cols[c].contains(dig) || boxes[b].contains(dig)) {
                    return false;
                } else {
                    rows[r].insert(dig);
                    cols[c].insert(dig);
                    boxes[b].insert(dig);
                }
            }
        }

        return true;


        
    }
};
