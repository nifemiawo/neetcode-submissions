class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rT = len(grid)
        cT = len(grid[0])
        count =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1 :
                    if i+1>= rT or grid[i+1][j] ==0:
                        count+=1
                    
                    if i-1<0 or grid[i-1][j] ==0:
                        count+=1
                    
                    if j+1 >= cT or grid[i][j+1] ==0:
                        count+=1
                    
                    if j-1 <0 or grid[i][j-1] ==0:
                        count+=1
        
        return count