class Solution {
public:

    int dfs(int curr,int i, int s,vector <int> nums){
        if (i>nums.size()-1)
            return false;
        if (curr == s - curr){
            return true;
        }
        return (dfs(curr+nums[i],i+1,s,nums) || dfs(curr,i+1,s,nums));
    }
    bool canPartition(vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if (s%2 == 1)
            return false;
        return dfs(0,0,s,nums);

    }
};
