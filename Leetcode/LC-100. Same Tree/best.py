
# Important question - teaches you to traverse two trees at same time.
# Earlier used the InOrder traversal way but it does not work for all cases.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare(node1, node2):
            # Base Case: both null
            if(node1 is None and node2 is None):
                return True

            # CASE 1: both exists
            if(node1 and node2):
                # Both same - valid, go deeper
                if(node1.val == node2.val):
                    isLeftSame = compare(node1.left, node2.left)
                    isRightSame = compare(node1.right, node2.right)
                    return isLeftSame and isRightSame
                # values differ of same position node
                else:
                    return False

            # CASE 2: any one exists - invalid positions
            else:
                return False
