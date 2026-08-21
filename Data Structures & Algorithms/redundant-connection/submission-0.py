class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)

        for u,v in edges:
            if not self.union(u,v):
                return [u,v]
        
        return None



    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,x,y):

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if self.rank[rootX] < self.rank[rootY]:
            rootX,rootY = rootY,rootX
        
        self.parent[rootY] = rootX

        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX]+=1
        
        return True


    
            