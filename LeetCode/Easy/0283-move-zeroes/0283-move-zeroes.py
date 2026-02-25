class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val=0
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
        
