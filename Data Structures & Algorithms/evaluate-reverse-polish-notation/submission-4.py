class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens: 
            if token == "+" and len(stack)>=2:
                n1 = stack.pop()
                n2 = stack.pop()
                tot = int(n1)+int(n2)
                stack.append(tot)
            elif token == "*" and len(stack) >=2:
                n1 = stack.pop()
                n2 = stack.pop()
                tot = int(n1) * int(n2)
                stack.append(tot)
            elif token == "-" and len(stack)>=2:
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(n2)-int(n1)
                stack.append(res)
            elif token == "/" and len(stack)>=2:
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(n2)/ int(n1)
                stack.append(res)
            else:
                stack.append(token)
        return int(stack[0])