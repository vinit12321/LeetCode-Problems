class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0 or n<0:
            return False
        
        while n>1:
            rem=n%2
            print("rem",rem)
            if rem==0:
                print(n)
                n=n/2
            else:
                print(n)
                return False
        return True
            
        