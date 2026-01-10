class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        
        while(low<=high):
            mid=(low+high)//2

            if nums[mid]==target:
                return mid
            

            if nums[low]<=nums[mid]:
                #left half
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1


            else:
                if nums[mid]<target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return -1


# l    l  m  h
# 5,6,7,3,2,1

# l      l  m h
# 4,5,6,7,0,1,2