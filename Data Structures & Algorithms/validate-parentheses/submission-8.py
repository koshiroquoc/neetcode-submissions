class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        key = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        if len (s) %2 == 1:
            return False
        ans = False
        for i in s:
            if i in "({[":
                stack.append(i)
            if not stack:
                return False
                
            if stack and i in ")}]":
                check = stack.pop()
                if key[check] == i: 
                    ans = True
                if key[check] != i:
                    return False
        if stack:
            return False
        return ans