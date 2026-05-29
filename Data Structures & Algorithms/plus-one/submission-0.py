class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. Convert the list of digits into an integer
        num = 0
        for i, v in enumerate(reversed(digits)):
            num += v * (10 ** i)
        
        # 2. Add one
        num += 1
        
        # 3. Convert the integer back into a list of digits
        # Using string conversion is the simplest way to handle this
        return [int(d) for d in str(num)]