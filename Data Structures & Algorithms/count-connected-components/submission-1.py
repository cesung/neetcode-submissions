class UnionFind:
    def __init__(self, n):
        self.rank = [1 for _ in range(n)]
        self.parent =  [i for i in range(n)]
    
    def find(self, v):
        root = v
        while self.parent[root] != root:
            root = self.parent[root]
        
        cur = v
        while cur != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt
        
        return root
    
    def union(self, v1, v2):
        r1, r2 = self.find(v1), self.find(v2)
        if r1 == r2:
            return
        
        if self.rank[r1] > self.rank[r2]:
            self.rank[r1] += self.rank[r2]
            self.parent[r2] = r1
        else:
            self.rank[r2] += self.rank[r1]
            self.parent[r1] = r2

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for n1, n2 in edges:
            uf.union(n1, n2)
        
        res = set()
        for i in range(n):
            res.add(uf.find(i))
        
        return len(res)