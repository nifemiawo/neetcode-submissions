class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            v1 = heapq.heappop(maxHeap)
            v2 = heapq.heappop(maxHeap)

            if v1 - v2 ==0:
                continue
            else:
                heapq.heappush(maxHeap,v1-v2)
        return -maxHeap[0] if len(maxHeap) > 0 else 0