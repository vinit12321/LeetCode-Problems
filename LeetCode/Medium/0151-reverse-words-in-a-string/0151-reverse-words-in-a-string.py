class Solution:
    def reverseWords(self, s: str) -> str:
        str_list=s.split()
        new_str=" ".join(str_list[::-1])        
        return new_str



                
            
            

            
        