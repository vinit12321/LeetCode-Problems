class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stk=[]
        for i,j in enumerate(temperatures):

            while stk and temperatures[stk[-1]]<j:

                v=stk.pop()
                res[v]=i-v
            stk.append(i)
               
        return res
            




            

        