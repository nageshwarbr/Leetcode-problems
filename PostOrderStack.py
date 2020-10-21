from collections import deque


class Solution:
    def post_order_stack(self, root):
        st1 = deque()
        st2 = deque()
        st1.append(root)
        ans = []
        while st1:
            x = st1.pop()
            st2.append(x)
            if x.left:
                st1.append(x.left)
            if x.right:
                st1.append(x.right)
        while st2:
            x = st1[-1]
            st1.pop(x)
            ans.append(x)

        return ans
