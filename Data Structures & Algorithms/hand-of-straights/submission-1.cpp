class Solution {
public:
    bool isNStraightHand(vector<int>& h, int g) {
        unordered_map<int, int> freq;
        for(auto i: h){
            freq[i]++;
        }
        sort(h.begin(),h.end());
        for(int i  = 0;i<=h.size();i++){
            if (i + 1 < (int)h.size() && h[i] == h[i+1])
                continue;
            while (freq[h[i]]){
                for(int j = h[i];j<h[i]+g;j++){
                    if (freq[j] == 0){
                        return false;
                    }
                    freq[j]--;
                }
            }
        }
        return true;
    }
};
