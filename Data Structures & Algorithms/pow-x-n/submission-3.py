class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x
        if n >0:
            while n > 1:
                ans = ans * x
                n = n-1
        elif n<0:
            while n<=0:
                ans = ans / x
                n = n+1 
        else:
            return 1
        
        return ans