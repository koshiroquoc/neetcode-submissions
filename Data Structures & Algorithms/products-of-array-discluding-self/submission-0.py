class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_thuan = [1]
        prefix_back = [1]
        for i in range (len(nums)-1):
            prefix_thuan.append(prefix_thuan[i]*nums[i]) 
        for i in range (len(nums)-1):
            prefix_back.insert(0, prefix_back[0]*nums[-(i+1)]) 
        ans = []
        for i in range (len(prefix_thuan)):
            ans.append(prefix_thuan[i] * prefix_back[i])
        return ans 