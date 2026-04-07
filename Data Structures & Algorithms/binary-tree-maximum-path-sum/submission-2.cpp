
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = root->val;
        dfs(root,res);
        return res;
    }
    int dfs(TreeNode* root,int &res){
        if (root == NULL)
            return 0;
        
        int lmax = dfs(root->left,res);
        int rmax = dfs(root->right,res);
        lmax = max(lmax,0);
        rmax = max(rmax,0);
        res = max(res,root->val + lmax + rmax);
        return root->val + max(lmax,rmax);

    }
};
