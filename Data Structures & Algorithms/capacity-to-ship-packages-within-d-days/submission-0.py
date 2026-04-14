class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        def check(n):
            t = 1
            s = 0
            for i in w:
                if s + i > n:
                    t+=1
                    s = 0

                s+=i
            print(days,t,n)
            if (t > days):
                return False
            return True

        lo = max(w)
        hi = sum(w)
        ans = 0
        while (lo<=hi):
            m = (lo+hi)//2
            if check(m):
                ans = m
                hi = m-1

            else:
                lo = m + 1

        return ans



