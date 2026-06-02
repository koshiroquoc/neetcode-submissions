class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs: 
            ans += str(len(i)) + "#" + i
        return ans 

    def decode(self, s: str) -> List[str]:
        length = 0 
        ans = []
        so = ""
        stop = -10
        for i in range (len(s)): 
            if i < stop:
                continue
            if s[i].isdigit():
                so += s[i]
            if s[i] == "#" and so != "":
                length = int(so)
                start = i+1
                stop = start + length
                ans.append(s[start:stop])
                so = ""
        return ans