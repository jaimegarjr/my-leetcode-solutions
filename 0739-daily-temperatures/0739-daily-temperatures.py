class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                stackTop = stack.pop()
                res[stackTop] = i - stackTop
            
            stack.append(i)
        
        return res