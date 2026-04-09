class Solution:
    def makesquare(self, m: List[int]) -> bool:
        s = sum(m)
        if s % 4 != 0:
            return False
        t = s // 4
        m.sort(reverse=True)
        
        def back(s1,s2,s3,s4,i):
            if i == len(m):
                if s1 == s2 == s3 == s4:
                    return True
                return False
            
            if s1 + m[i] <= t:
                if back(s1+m[i],s2,s3,s4,i+1): return True
            if s2 + m[i] <= t and s2 != s1:
                if back(s1,s2+m[i],s3,s4,i+1): return True
            if s3 + m[i] <= t and s3 != s2 and s3 != s1:
                if back(s1,s2,s3+m[i],s4,i+1): return True
            if s4 + m[i] <= t and s4 != s3 and s4 != s2 and s4 != s1:
                if back(s1,s2,s3,s4+m[i],i+1): return True
            return False
        
        return back(0,0,0,0,0)