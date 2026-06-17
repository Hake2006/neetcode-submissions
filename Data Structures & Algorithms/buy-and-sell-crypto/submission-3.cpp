class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mp = 0;
        int mb = prices[0];
        for (int& p:prices){
            mp = max(mp,p-mb);
            mb = min(mb,p);
        }
        return mp;
    }
};
