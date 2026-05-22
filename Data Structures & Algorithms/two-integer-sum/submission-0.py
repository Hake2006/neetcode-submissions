class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pi = {}
        for i,v in enumerate(nums):
            if target - v in pi:
                if i<= pi[target-v]:
                    return [i,pi[target-v]]
                else:
                    return [pi[target-v],i]
            pi[v] = i