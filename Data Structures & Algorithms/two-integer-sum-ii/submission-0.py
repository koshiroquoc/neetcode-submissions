class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        found = 0
        while found == 0 :
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left +=1 
            if numbers[left] + numbers[right] == target: 
                found = 1
        return [left + 1, right +1]
