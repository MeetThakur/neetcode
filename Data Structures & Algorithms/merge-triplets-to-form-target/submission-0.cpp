class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        bool first=false;
        bool second=false;
        bool third=false;
        for(const vector<int>&cand: triplets){
            if(cand[0]>target[0] || cand[1]>target[1] || cand[2]>target[2])continue;
            if(cand[0]==target[0])first=true;
            if(cand[1]==target[1])second=true;
            if(cand[2]==target[2])third=true;

        }
        return first&&second&&third;
    }
};