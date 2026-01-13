class Solution:
    def secondHighest(self, s: str) -> int:
        secondMaximum=-1
        maximum=-1
        for i in range(len(s)):
            if s[i].isdigit():
                val=int(s[i])
                if maximum<val:
                    secondMaximum=maximum
                    maximum=val
                elif secondMaximum<val and val < maximum:
                    secondMaximum=val
        return secondMaximum


            
        