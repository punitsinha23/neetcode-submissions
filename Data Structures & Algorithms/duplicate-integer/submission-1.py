class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = {} 
        for n in nums:
            if n in num:
                num[n] += 1
                return True
            else:    
                num[n] = 1  
        return False                


         