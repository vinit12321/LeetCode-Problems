class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st={}
        tt={}
        if(len(s) != len(t)):
            return False;
        for i in range(len(s)):
            st[s[i]]=1+st.get(s[i],0)
            tt[t[i]]=1+tt.get(t[i],0)
        
        for j in st:
            if st[j] !=tt.get(j,0):
                return False;
            
        return True
        