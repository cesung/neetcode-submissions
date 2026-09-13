class Solution:
    def dfs(self, c, graph, vis):
        if vis[c] == 1:
            return False
        elif vis[c] == 2:
            return True
        
        # mark as visiting
        vis[c] = 1

        for nxt in graph[c]:
            if not self.dfs(nxt, graph, vis): 
                return False

        # mark as done visited
        vis[c] = 2
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        # 0: not yet visit
        # 1: visiting
        # 2: done visited
        vis = {i : 0 for i in range(numCourses)}

        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        
        for c in range(numCourses):
            if not self.dfs(c, graph, vis):
                return False

        return True