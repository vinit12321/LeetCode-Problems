class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0] in (')','}',']') :
            return False
    
        for i in range(len(s)):
            if s[i] in ('(','[','{'):
                stack.append(s[i])
            elif s[i] in (')',']','}') and len(stack)!=0:
                ele=stack.pop()
                if s[i]==')' and ele!='(':
                    return False
                
                elif s[i]==']' and ele!='[':
                    return False
                
                elif s[i]=='}' and ele!='{':
                    return False
            else:
                return False
        
        if len(stack)==0:
            return True
        else:
            return False

