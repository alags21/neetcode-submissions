class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_set<char>> boxes;

        int curr_box = 0;
        for (int row = 0; row <= 8; row++) {
            for (int col = 0; col <= 8; col++) {
                char current = board[row][col];
                if (current == '.') continue;

                curr_box = (row / 3) * 3 + (col / 3);
                if (rows[row].contains(current)) return false;
                rows[row].emplace(current);
                if (cols[col].contains(current)) return false;
                cols[col].emplace(current);
                if (boxes[curr_box].contains(current)) return false;
                boxes[curr_box].emplace(current);
            }
        }
        return true;

    }
};
