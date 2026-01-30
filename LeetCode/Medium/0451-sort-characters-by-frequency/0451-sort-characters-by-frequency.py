class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        x=Counter(s)
        data=""
        for i,j in x.most_common():
            data+=''.join(i*j)
        return data

