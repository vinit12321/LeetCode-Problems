class Solution:
    def isPalindrome(self, x: int) -> bool:
         
        s = str(x)
        rtl = ''
        for i in s:
            rtl = i + rtl
        return s == rtl