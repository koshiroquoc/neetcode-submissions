class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        value = {}
        for i in s:
            if i not in value: 
                value[i] = 0 
            value[i] +=1 
        for i in t:
            if i not in value:
                return False
            value[i] -=1 
        return all(value == 0 for value in value.values())
            