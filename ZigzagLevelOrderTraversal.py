import collections


class Solution:
    def zigzagLevelOrder(self,root):
        if root is None:
            return []
        res=[]
        q=collections.deque()

        zigzag=False
        q.append(root)

        while q:
            level=[]

            for _ in range(len(q)):
                if zigzag:
                    node=q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                else:
                    node=q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            res.append(level)
            zigzag=not zigzag

        return res

