class UnionFind:
    def __init__(self, n):
        self.rank = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]
    
    def find(self, v):
        root = v
        while self.parent[root] != root:
            root = self.parent[root]
        
        cur = v
        while self.parent[cur] != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt
        
        return root

    def union(self, v1, v2):
        r1, r2 = self.find(v1), self.find(v2)
        if r1 == r2:
            return False
        
        if self.rank[r1] > self.rank[r2]:
            self.rank[r1] += self.rank[r2]
            self.parent[r2] = r1
        else:
            self.rank[r2] += self.rank[r1]
            self.parent[r1] = r2
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        res = set()
        for v1, v2 in edges:
            if uf.union(v1, v2) == False:
                return False
        
        for v in range(n):
            res.add(uf.find(v))
        
        return len(res) == 1
        