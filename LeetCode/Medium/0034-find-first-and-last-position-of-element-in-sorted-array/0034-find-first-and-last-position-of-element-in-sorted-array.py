class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lower_bound(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans


        def higher_bound(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans

        left=lower_bound(nums,target)
        right=higher_bound(nums,target)
        return [left,right]