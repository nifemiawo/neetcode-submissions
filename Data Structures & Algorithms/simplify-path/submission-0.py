class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]
        path = path.split("/")
        ans=""
        for c in path:
            if c == "." or c == "":
                continue
            
            elif c == "..":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(c)
        
        if len(stack)==0:
            return "/"
        
        for c in stack:
            ans+="/"+c
        
        return ans