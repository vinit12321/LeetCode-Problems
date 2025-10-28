class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}
        for i in range(len(nums)):
            if target-nums[i] in data:
                return [ data.get(target-nums[i]), i ]
            data[nums[i]]=i
        return [-1,-1]


