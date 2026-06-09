class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        left = 0 
        ans = 0
        for right in range (len(s)):
            if s[right] not in check:
                check[s[right]] = 1
            else:
                check[s[right]] +=1 
            while (right - left + 1) - max(check.values()) > k:
                check[s[left]] -=1
                left +=1 
            ans = max (ans, right - left + 1)
        return ans