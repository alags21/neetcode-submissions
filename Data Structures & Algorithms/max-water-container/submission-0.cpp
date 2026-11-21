class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i = 0;
        int j = heights.size() - 1;
        int currmax = 0;
        while (i < j) {
            int currprod = (j-i) * (max(heights[i], heights[j]), min(heights[i], heights[j]));
            if (currprod > currmax) {
                currmax = currprod;
            }
            
            if (heights[i] < heights[j]) {
                i++;
            } else if (heights[i] > heights[j]) {
                j--;
            } else{
                i++;
            }
        }
        return currmax;
    }
};
