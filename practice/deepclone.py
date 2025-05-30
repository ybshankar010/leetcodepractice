"""
# Definition for a Node.
"""
from collections import deque

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node: return node

        nodes_arr = [None for _ in range(102)]

        visited = set()
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            visited.add(curr.val)
            # print(visited)

            new_node = nodes_arr[curr.val]
            if not new_node:
                new_node = Node(node.val,None)
            
            nodes_arr[curr.val] = new_node
            neighbors = curr.neighbors
            if not neighbors:
                continue

            new_neighbors = []
            for neighbor in neighbors:
                new_neighbor = nodes_arr[neighbor.val]
                if not new_neighbor:
                    new_neighbor = Node(neighbor.val, None)
                    nodes_arr[neighbor.val] = new_neighbor
                
                if neighbor.val not in visited:
                    queue.append(neighbor)
                
                new_neighbors.append(new_neighbor)

            new_node.neighbors = new_neighbors
            nodes_arr[curr.val] = new_node

        # adjacency_list = []
        # for new_node in nodes_arr:
        #     if not new_node or not new_node.neighbors:
        #         continue
        #     print(new_node.val,"<>",(','.join(str(node.val) for node in new_node.neighbors)))
        #     adjacency_list.append(new_node.neighbors)
        
        # print('\n'.join(' '.join(str(cell.val) for cell in row) for row in adjacency_list))
        return nodes_arr[node.val]