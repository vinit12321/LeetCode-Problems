class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n==0 or n<0:
        #     return False
        
        # while n>1:
        #     rem=n%2
        #     print("rem",rem)
        #     if rem==0:
        #         n=n/2
        #     else:
        #         return False
        # return True

        return n>0 and (n & (n-1)==0)
            
        