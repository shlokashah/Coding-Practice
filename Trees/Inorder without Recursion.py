class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        current = A
        stack = []
        answer = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                answer.append(current.val)
                current = current.right
            else:
                break
        return answer