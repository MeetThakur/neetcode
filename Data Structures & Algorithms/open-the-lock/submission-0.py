class Solution:
    def openLock(self, d: List[str], target: str) -> int:
        if "0000" in d:
            return -1

        def help(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque()
        turn = 0
        q.append(("0000",0))
        vis = set()
        for i in d:
            vis.add(i)
        while q:
            l , t = q.popleft()
            if l == target:
                return t
            
            for nx in help(l):
                if nx not in vis:
                    vis.add(nx)
                    q.append((nx,t+1))
        return -1