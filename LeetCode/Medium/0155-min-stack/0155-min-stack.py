class MinStack:

    def __init__(self):
        self.st=[]
        self.mini=None

    def push(self, val: int) -> None:
        if not self.st  :
            self.mini=val
            self.st.append(val)
            return
        
        if val > self.mini:
            self.st.append(val)
        else:
            diff=2*val-self.mini
            self.st.append(diff)
            self.mini=val

        



    def pop(self) -> None:
        if not self.st:
            return 
        
        val=self.st.pop()
        if val < self.mini:
            self.mini=2*self.mini -val
        

    def top(self) -> int:
        if not self.st:
            return -1
        val=self.st[-1]
        if self.mini < val:
            return val
        return self.mini

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()