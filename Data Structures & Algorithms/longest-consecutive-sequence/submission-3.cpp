class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(),nums.end());
        int res=0,cur=nums[0],stk=0,i=0;
        while (i<nums.size()){
            if (cur!=nums[i]){
                cur = nums[i];
                stk = 0;
            }
            while(i<nums.size()&&nums[i]==cur){
                i++;
            }
            stk++;
            cur++;
            res = max(res,stk);
        }
        return res;
    }
};
