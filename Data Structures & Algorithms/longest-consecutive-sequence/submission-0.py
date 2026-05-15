class Solution:
    def longestConsecutive(self, nums: List[int]):
        sorted_arr = sorted(set(nums))
        len_arr = len(sorted_arr)
        checker = 1
        max_streak = 0
        for i, num in enumerate(sorted_arr):
            if i < len_arr - 1 and num + 1 == sorted_arr[i + 1]:
                checker += 1
                print(checker)
            else:
                max_streak = max(max_streak , checker)
                checker = 1 
        return max_streak                  
        