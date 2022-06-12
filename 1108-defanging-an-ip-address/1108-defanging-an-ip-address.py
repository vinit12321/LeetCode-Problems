class Solution:
    def defangIPaddr(self, address: str) -> str:
        newstr=""
        for i in range(len(address)):
            if address[i]=='.':
                newstr+="["+address[i]+"]"
            else:
                newstr+=address[i]
        return newstr
        
        