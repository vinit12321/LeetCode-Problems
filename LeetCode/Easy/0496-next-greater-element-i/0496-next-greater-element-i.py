class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={n:i for i,n in enumerate(nums1)}
        n=len(nums1)
        res=[-1] * n
        stk=[]
        for i in range(len(nums2)):

            cur=nums2[i]
            while stk and stk[-1] < cur:
                ele=stk.pop()
                index=dict1[ele]
                res[index]=cur
            
            if nums2[i] in dict1:
                stk.append(nums2[i])
            
        return res