class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        for i in range(1,len(nums)+1):
            xor1=xor1^i
        xor2=0
        for data in nums:
            xor2=xor2^data
        missing=xor1^xor2
        return missing

        