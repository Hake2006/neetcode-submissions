class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int l=0,r=n-1,ans=0;
        while(l<r){
            int wtr = min(heights[l],heights[r])*(r-l);
            ans = max(ans,wtr);
            if (heights[l]<=heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return ans;
    }
};
