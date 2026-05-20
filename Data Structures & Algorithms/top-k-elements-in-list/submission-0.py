class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        return sorted(d.keys(),key=lambda x:d[x])[-k:]
        