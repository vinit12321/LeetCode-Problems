class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1={}
        for i in range(len(nums)):
            if target-nums[i]  in dict1:
                dif=target-nums[i]
                return [dict1[dif],i]
            dict1[nums[i]]=i
