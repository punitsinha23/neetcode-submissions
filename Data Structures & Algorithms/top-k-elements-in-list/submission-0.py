class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dic = {}
        for num in nums:
            Dic[num] = Dic.get(num, 0) + 1  
        
        
        top_k = sorted(Dic.keys(), key=lambda num: Dic[num], reverse=True)[:k]
        
        return top_k