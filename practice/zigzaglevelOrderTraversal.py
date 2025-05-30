from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return []

        level_one_queue = deque([root])
        level_two_queue = deque()
        zigzag_levels = []
        left_to_right = False

        while level_one_queue:
            # print(level_one_queue)
            level = []
            for _ in range(len(level_one_queue)):
                curr = level_one_queue.popleft()
                level.append(curr.val)
                if curr.left: level_one_queue.append(curr.left)
                if curr.right: level_one_queue.append(curr.right)

            if left_to_right: level.reverse()
            zigzag_levels.append(level)
            left_to_right = not left_to_right
        
        return zigzag_levels


# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.zigzagLevelOrder(None))