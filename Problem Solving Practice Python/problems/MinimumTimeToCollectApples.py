'''
1443. Minimum Time to Collect All Apples in a Tree
Solved
Medium
Topics
Companies
Hint
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

'''

def minTime(n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adjacency_list = {i:[]for i in range(n)}
        for parent, child in edges:
            adjacency_list[parent].append(child)
            adjacency_list[child].append(parent)
        def dfs(current, parent):
            time = 0
            for children in adjacency_list[current]:
                if children == parent:
                    continue
                childrenTime = dfs(children, current)
                if childrenTime or hasApple[children]:
                    time += 2 + childrenTime
            return time
        return dfs(0,-1)