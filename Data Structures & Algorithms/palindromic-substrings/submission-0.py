class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i,s,even = True,c=0):
            if even == True:
                l = i
                r = i+1
            if even == False:
                l = i
                r  = i
            if l<0 or r>len(s)-1:
                return c
            while(s[l]==s[r]):
                print(s[l:r+1])
                l-=1
                r+=1
                c+=1
                if l<0 or r>len(s)-1:
                    break
            return c
        c = 0
        for i in range(len(s)):
            c += expand(i,s,True,0)
            c += expand(i,s,False,0)
        return c



                    
                
