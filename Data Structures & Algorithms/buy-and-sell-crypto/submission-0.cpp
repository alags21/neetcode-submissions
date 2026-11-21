class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProf = 0;
        int minPrice = prices[0];
        for (int i=1; i < prices.size(); i++) {
            int curr = prices[i];
            minPrice = min(minPrice, curr);
            int diff = prices[i] - minPrice;
            maxProf = max(diff, maxProf);
        }
        return maxProf;
    }
};
