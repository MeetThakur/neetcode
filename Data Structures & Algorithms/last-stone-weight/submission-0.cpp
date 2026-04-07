class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for(auto i:stones){
            pq.push(i);
        }
        int x,y;
        while(pq.size()>1){
            x = pq.top();
            pq.pop();
            y = pq.top();
            pq.pop();
            if(x==y)
                continue;
            else
                pq.push(max(x,y)-min(x,y));
        }
        if (pq.size())
            return pq.top();
        return 0;
    }
};   