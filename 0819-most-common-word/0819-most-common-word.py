class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        str1=""
        dict={}
        for s in paragraph:
            if s.isalnum():
                str1+=s.lower()
            else:
                if str1 not in dict and str1!="":
                    dict[str1]=1
                elif str1 in dict and str1!="":
                    dict[str1]+=1
                str1=""
        if str1 not in dict:
            dict[str1]=1
        else:
            dict[str1]+=1
        
        for i in banned:
            if i in dict:
                del dict[i]
        print(dict)
        max=0
        max_key=None
        for key,value in dict.items():
            if value>max:
                max=value
                max_key=key
        return max_key
            


        