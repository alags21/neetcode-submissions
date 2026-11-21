class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int max_size = 0;
        // container size = (r-l) * min(heights[l], heights[r])
        while (l < r) {
            int container_size = (r-l) * min(heights[l], heights[r]);
            max_size = max(max_size, container_size);
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_size;
    }
};
