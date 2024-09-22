
# Time: O(n)
# Using HBI(Hypothesis, Base Condition, Induction)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(node):
            if(node is None):
                return []
            
            left = inOrder(node.left)
            right = inOrder(node.right)
            # appending current node value
            left.append(node.val) 
            # appending right subTree values
            left.extend(right)
            # returning the package
            return left
        
        # implementing
        return inOrder(root)
