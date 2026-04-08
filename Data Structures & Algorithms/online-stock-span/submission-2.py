class StockSpanner:
    def __init__(self):
        self.st = []


    def next(self, p: int) -> int:
        if not self.st:
            self.st.append([p,1])
            return 1
        
        sp = 1
        if p >= self.st[-1][0]:    
            while(self.st and self.st[-1][0] <= p):
                t = self.st.pop()
                sp += t[-1]

            self.st.append([p,sp])
            return sp      
        self.st.append([p,1])
        return 1