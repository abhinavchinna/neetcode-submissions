class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for i in range(len(nums)):
            if target-nums[i] not in d:
                d[nums[i]]=i
            else:
                return sorted([d[target-nums[i]],i])
        