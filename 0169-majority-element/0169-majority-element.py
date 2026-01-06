class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for n in nums:
            if n in dict1:
                dict1[n]+=1
            else:
                dict1[n]=1

        for key,value in dict1.items():
            if value > int(len(nums)/2):
                return key
                
            

        