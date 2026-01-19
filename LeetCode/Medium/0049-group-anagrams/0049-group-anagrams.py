from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data=defaultdict(list)
        for s in strs:
            s1=''.join(sorted(s))
            data[s1].append(s)
        return list(data.values())