class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        # Traverse from second element
        for i in range(1, len(nums)):
            curr = nums[i]

            # Swap max and min if current is negative
            if curr < 0:
                maxProd, minProd = minProd, maxProd

            # Update max and min product
            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)

            # Update result
            res = max(res, maxProd)

        return res


        