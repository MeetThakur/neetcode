class Solution {
public:
    vector <vector<int>> ans;

    void back(int n,int k, vector<int> curr, int c){
        if (curr.size() == k) {
            ans.push_back(curr);
            return;
        }
            

        if (c==n+1)
            return;
        
        curr.push_back(c);
        back(n,k,curr,c+1);
        curr.pop_back();
        back(n,k,curr,c+1);
        return ;

    }
    vector<vector<int>> combine(int n, int k) {
        ans.clear();
        back(n,k,{},1);
        return ans;
    }
};