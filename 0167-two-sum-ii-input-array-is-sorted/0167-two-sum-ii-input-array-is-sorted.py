class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1

        while i<j:
            currSum = numbers[i]+numbers[j]

            if currSum == target:
                break

            if currSum > target:
                j-=1
            else:
                i+=1
        
        return [i+1, j+1]