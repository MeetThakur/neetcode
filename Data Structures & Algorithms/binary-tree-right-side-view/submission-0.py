# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        curr = [root]
        if root == None:
            return []
        ans = [root.val]
        
        while curr:
            t = []
            k = []
            for i in curr:
                if i.left:
                    k.append(i.left.val)
                    t.append(i.left)
                if i.right:
                    k.append(i.right.val)
                    t.append(i.right)
            if k:
                ans.append(k[-1])
            curr = t
        return ans
            