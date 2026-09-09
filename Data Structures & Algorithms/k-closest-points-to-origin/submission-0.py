class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for p in points:
            distance = p[0] * p[0] + p[1]*p[1]
            heapq.heappush(heap, (-distance,p[0],p[1]))
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        for d,x,y in heap:
            res.append([x,y])
        
        return res

        