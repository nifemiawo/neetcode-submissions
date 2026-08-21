class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        currRun =1
        maxRun=1
        best=1
        direction="none"

        for i in range(1,len(arr)):
            #asc
            if arr[i] > arr[i-1]:
                if direction == "none":
                    currRun = 2
                elif direction == "up":
                    currRun =2
                else:
                    currRun+=1
                direction = "up"
            elif arr[i] < arr[i-1]:
                if direction == "none":
                    currRun = 2
                elif direction == "down":
                    currRun =2
                else:
                    currRun+=1
                direction = "down"
            else:
                if direction == "none":
                    currRun=1
                elif direction == "flat":
                    currRun =1
                else:
                    currRun=1
                direction = "none"
            best = max(best,currRun)
        
        return best
            
