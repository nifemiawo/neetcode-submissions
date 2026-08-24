class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res =[0] * len(temperatures)

        for i,val in enumerate(temperatures):

            while stack and val > temperatures[stack[-1]] :
                idx = stack.pop()
                res[idx] = i-idx
            stack.append(i)
            
        return res