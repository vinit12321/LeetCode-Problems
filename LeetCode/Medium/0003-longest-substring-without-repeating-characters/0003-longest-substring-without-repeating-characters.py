class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        for i in range(len(s)):

            new_data={}
            new_data[s[i]]=1
            for j in range(i+1,len(s)):
                if s[j] not in new_data:
                    new_data[s[j]]=1
                else:
                    break
            num=len(new_data.keys())

            if num>max:
                max=num
            
        return max
