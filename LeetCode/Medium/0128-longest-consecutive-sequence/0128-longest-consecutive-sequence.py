class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        max_cnt=0
        for j in st:
            count=1
            num=j
            if num-1 not in st:
                while num+1  in st:
                    count+=1
                    num+=1

                max_cnt=max(count,max_cnt)
        return max_cnt