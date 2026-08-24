class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
       
        for val in asteroids:
            alive = True
            if val > 0:
                stack.append(val)
                
                continue
            
            while stack and stack[-1] > 0 and val <0:
                if abs(val) > stack[-1]:
                    stack.pop()
                    
                elif abs(val) < stack[-1]:
                    alive = False
                    break
                else:
                    
                    stack.pop()
                    alive = False
                    break
            
            if alive:
                stack.append(val)
        return stack
