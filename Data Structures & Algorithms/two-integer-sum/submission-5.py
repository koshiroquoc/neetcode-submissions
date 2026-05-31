class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for index, value in enumerate(nums):
            goal = target - value 
            if goal not in seen:
                seen[value] = index 
            else:
                return [seen[goal], index]