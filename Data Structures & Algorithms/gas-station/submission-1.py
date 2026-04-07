class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        ans = 0
        t = 0
        for i in range(len(gas)-1):
            ans += gas[i] - cost[i]
            if ans<0:
                t = i+1
                ans=0
        return t

