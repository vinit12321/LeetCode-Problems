class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1=defaultdict(list)
        for s in strs:
            counter=[0] * 26

            for ch in s:
                counter[ord(ch) - ord('a')]+=1
            dict1[tuple(counter)].append(s)
        return list(dict1.values())
            