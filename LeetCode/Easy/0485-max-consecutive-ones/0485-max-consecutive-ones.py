class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxi=float('-inf')
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            elif nums[i]==0:
                cnt=0
            maxi=max(cnt,maxi)
        return maxi