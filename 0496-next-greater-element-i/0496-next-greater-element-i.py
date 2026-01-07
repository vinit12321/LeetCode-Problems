class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={n:i for i,n in enumerate(nums1)}
        n=len(nums1)
        res=[-1] * n
        for i in range(len(nums2)):
            if nums2[i] not in dict1:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    index=dict1[nums2[i]]
                    res[index]=nums2[j]
                    break
        return res