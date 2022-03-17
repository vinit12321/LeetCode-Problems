class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        num1="".join(map(str, num))
        value=int(num1)+k
        return list(map(int, str(value)))
        