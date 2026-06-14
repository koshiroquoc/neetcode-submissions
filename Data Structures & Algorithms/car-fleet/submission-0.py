class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        car = list(zip(position,speed))
        car.sort(reverse = True)
        for pos, sped in car:
            time.append((target  - pos) / sped)

        stack = [] 
        stack.append(time[0])
        count = 1
        
        for i in range (1,len(time)):
  
            if stack and time[i] <= stack[-1]:
                continue 
            if stack and time [i] > stack[-1]:
                stack.pop()
                stack.append(time[i])
                count +=1

        return count