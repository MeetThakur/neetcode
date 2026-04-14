class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        
        while True:
            m = (l + r) // 2
            
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m - 1
            else:
                l = m + 1