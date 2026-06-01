class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        longest = 0 
        start = -1000
        maxx = 1 
        ans = {}
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        for i in range (len(nums)): 
            if nums[i] - 1 not in nums: 
                start = nums[i]
            if nums[i] == start + longest + 1:
                longest +=1
                ans[start] = longest + 1 
        for value in ans.values():
            if value >= maxx:
                maxx = value 
        return maxx