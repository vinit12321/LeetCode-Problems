class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set()
        for i in nums:
            numset.add(i)
    
        longest=1
        if len(nums)==0:
            return 0
        
        for n in nums:

            if n-1 not in numset:

                cnt=1
                curr=n
                while curr+1 in numset:
                    cnt+=1
                    curr+=1

                longest=max(longest,cnt)
        return longest