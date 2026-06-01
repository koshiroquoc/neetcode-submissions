class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for i  in nums: 
            if i not in mapp:
                mapp[i] = 1
            else:
                mapp[i] +=1 
        sorted_mapp = dict(sorted(mapp.items(), key=lambda x: x[1], reverse=True))
        ans = list(sorted_mapp.keys())
        anss= []
        for i in range (k):
            anss.append(ans[i])
        return anss