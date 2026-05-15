from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        arr = sorted(nums)
    
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                arr_sum = arr[left] + arr[right] + arr[i]
                if arr_sum < 0:
                    left += 1
                elif arr_sum > 0:
                    right -= 1
                else:
                    result.append([arr[i], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left + 1]: 
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1        
        return result   