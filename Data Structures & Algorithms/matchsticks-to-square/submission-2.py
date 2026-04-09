class Solution:
    def makesquare(self, m: List[int]) -> bool:
        def back(s1,s2,s3,s4,i):
            if i == len(m):
                if s1 == s2 == s3 == s4:
                    return True
                return False

            if max(s1,s2,s3,s4) > s/4:
                return False

            t1 = t2 = t3 = t4 = False
            if s1 + m[i] <= s/4:
                t1 = back(s1+m[i],s2,s3,s4,i+1)
            if s2 + m[i] <= s/4 and s2!=s1:
                t2 = back(s1,s2+m[i],s3,s4,i+1)
            if s3 + m[i] <= s/4 and s3 != s1 and s3 != s2:
                t3 = back(s1,s2,s3+m[i],s4,i+1)
            if s4 + m[i] <= s/4 and s4 != s1 and s4 != s2 and s4 != s3:
                t4 = back(s1,s2,s3,s4+m[i],i+1)
            
            return t1 or t2 or t3 or t4        
        s = sum(m)
        m.sort(reverse=True)
        return back(0,0,0,0,0)