class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = int(tokens[0])
        stack = []
        for i in range (len(tokens)):
            if stack and tokens[i] in "+-*/":
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                if tokens[i] == "+":
                    ans = int(temp2)+int(temp1)
                    stack.append(ans) 
                if tokens[i] == "-":
                    ans = int(temp2) - int(temp1)
                    stack.append(ans)
                if tokens[i] == "*":
                    ans = int(temp2) * int(temp1)
                    stack.append(ans)
                if tokens[i] == "/":
                    ans = int(temp2) / int(temp1)
                    stack.append(ans)
            else: 
                stack.append(int(tokens[i]))
        return int(ans)