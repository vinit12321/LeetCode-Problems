class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        si={}
        for i,n in enumerate(nums):
            if((target-n) in si):
                return [si[target-n],i]
            si[n]=i;
        return [0,0]
        