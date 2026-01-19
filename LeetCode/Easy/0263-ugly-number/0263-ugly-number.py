class Solution:
    def isUgly(self, n: int) -> bool:
        out=[2,3,5]
        if n <= 0:
            return False
 
        for num in out:
            while n%num==0:
                n=n//num
        
        return n==1
                

            
                
            
        