class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        int mid;
        while (l <= r) {
            mid = l + (r - l) / 2;
            long long sum = 0;
            for (int n : piles) {
                sum = sum + (n/mid) + (n % mid != 0);
            }

            if (sum > h) {
                l = mid+1;
            } else {
                r = mid-1;
            }
        }
    return l;
    }
};
