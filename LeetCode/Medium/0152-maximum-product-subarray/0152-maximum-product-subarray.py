class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod=nums[0]
        max_prod=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            curr=nums[i]
            if curr < 0:
                min_prod,max_prod=max_prod,min_prod
            
            min_prod=min(curr,min_prod*curr)
            max_prod=max(curr,max_prod*curr)
            res=max(res,max_prod)
        return res
            


        