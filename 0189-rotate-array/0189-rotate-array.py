class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Brute Force
        # n=len(nums)
        # for i in range(k):
        #     temp=nums[n-1]
        #     for j in range(n-1,0,-1):
        #         nums[j]=nums[j-1]
        #     nums[0]=temp

        # return nums
        #First Reverse array 

        def reverse_array(arr,start,end):
            n=len(arr)
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1

        n=len(nums)
        k=k%n
        reverse_array(nums,0,n-1)
        # First D part

        reverse_array(nums,0,k-1)
        # Next part after D

        reverse_array(nums,k,n-1)

    
        

