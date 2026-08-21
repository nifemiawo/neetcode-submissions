class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.count =n
        self.parent=list(range(n))
        self.rank = [1] *n

        for u,v in edges:
            if self.find(u) != self.find(v):
                self.union(u,v)
                self.count-=1
        
        return self.count

    def find(self,x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,x,y):

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return
        
        if self.rank[rootX] < self.rank[rootY]:
            rootX,rootY = rootY, rootX
        
        self.parent[rootY] = rootX

        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX]+=1
