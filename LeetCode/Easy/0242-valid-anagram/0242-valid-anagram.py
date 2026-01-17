class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1
        
        for j in range(len(t)):
            if t[j] in dict1:
                dict1[t[j]]-=1
            else:
                return False
        
        for k,v in dict1.items():
            if v!=0:
                return False
        return True
                
        
