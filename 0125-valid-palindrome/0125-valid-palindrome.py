class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        result = True

        while(i<j):
            while(i<len(s) and not s[i].isalnum()):
                i+=1
            while(j>=0 and not s[j].isalnum()):
                j-=1
            
            if i>=len(s) and j<0:
                break
            
            if(s[i].lower()==s[j].lower()):
                i+=1
                j-=1
            else:
                result=False
                break
        
        return result