

# Not the best solution with Recursion
# Try: Using Queue for best

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def minimumDepth(node):
            if(node is None):
                return 0
            leftSubTreeMinDepth = minimumDepth(node.left)
            rightSubTreeMinDepth = minimumDepth(node.right)

            # if leftSubTree is empty then it will be considered minimum depth but it should be neglected
            # as its null node
            if(leftSubTreeMinDepth == 0):
                return 1 + rightSubTreeMinDepth
            if(rightSubTreeMinDepth == 0):
                return 1 + leftSubTreeMinDepth

            return 1 + min(leftSubTreeMinDepth, rightSubTreeMinDepth)
        
        # implementing
        return minimumDepth(root)
        
