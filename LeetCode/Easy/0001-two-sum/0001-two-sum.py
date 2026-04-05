class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data={}

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff not in data:
                data[nums[i]]=i
            else:
                #print(data)
                return [data[diff],i]
        return [-1,-1]
            