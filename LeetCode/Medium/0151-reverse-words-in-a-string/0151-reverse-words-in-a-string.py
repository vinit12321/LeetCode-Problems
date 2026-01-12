class Solution:
    def reverseWords(self, s: str) -> str:
        str_list=s.split()
        new_str=""
        print(str_list)
        for i in range(len(str_list)-1,-1,-1):
            
            new_str+=str_list[i]
            if i !=0:
                new_str+=" "
        return new_str



                
            
            

            
        