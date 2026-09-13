class Solution:
    def dfs(self, graph, vis, c):
        if vis[c] == 1:
            return False
        if vis[c] == 2:
            return True
        
        vis[c] = 1

        for nc in graph[c]:
            if not self.dfs(graph, vis, nc):
                return False
            
        vis[c] = 2
        self.order.append(c)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        # 0: not yet visit
        # 1: visiting
        # 2: visited
        vis = {i:0 for i in range(numCourses)}
        self.order = []

        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        
        for i in range(numCourses):
            if vis[i] == 0 and not self.dfs(graph, vis, i):
                return []
        
        return self.order