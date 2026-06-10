class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check1 ={}
        for i in s1:
            check1[i] = check1.get(i, 0) + 1

        if len(s1) > len(s2):
            return False

        left = 0
        found = False
        for right in range(len(s1),len(s2)+1):
            need = s2[left:right]
            check2 = check1.copy() 
            
            for i in need:
                if i not in check2:  
                    break 
                check2[i] -=1 
                found = all(value == 0 for value in check2.values())
            if found == True:
                return True
            left +=1 
        return found 