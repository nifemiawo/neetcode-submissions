class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]

        for op in operations:
            if op == "+" and len(stack)>0:
                n1 = stack.pop()
                n2 = stack.pop()
                tot = n1+n2
                stack.append(n2)
                stack.append(n1)
                stack.append(tot)
            elif op == "C" and len(stack) >0:
                stack.pop()
            elif op == "D" :
                el = stack[-1]
                ans = 2*el
                stack.append(ans)
            else:
                stack.append(int(op))
        
        tot =0
        for num in stack:
            tot+=num
        return tot
