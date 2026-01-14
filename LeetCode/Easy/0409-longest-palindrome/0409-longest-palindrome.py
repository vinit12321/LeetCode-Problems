class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1

            
        max_sum=0
        if len(s)==1:
            return 1
        
        for key,val in dict1.items():
            if val%2==0:
                max_sum+=val
            elif val%2!=0 and val!=1:
                max_sum+=val-1
                dict1[key]=val-(val-1)
        print(max_sum)
        for key,val in dict1.items():
            if val%2!=0:
                max_sum+=1
                break
        return max_sum
