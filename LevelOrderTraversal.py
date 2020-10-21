from collections import deque


class Solution:
    def levelOrder(self, root):
        ans = []

        if root is None:
            return ans
        q = deque([root])

        while q:
            n = len(q)
            temp = []

            for i in range(0, n):
                f = q.popleft()
                temp.append(f.val)
                if f.left is not None:
                    q.append(f.left)
                elif f.right is not None:
                    q.append(f.right)

            if len(temp > 0):
                ans.append(temp[:])
                temp.clear()
        return ans
