class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        max_cnt=0
        for j in range(len(nums)):
            if nums[j]==1:
                cnt+=1
            else:
                cnt=0
            max_cnt=max(cnt,max_cnt)
        return max_cnt