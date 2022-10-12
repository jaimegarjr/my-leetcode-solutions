class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for curDay, curTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curTemp:
                prevDay = stack.pop()
                res[prevDay] = curDay - prevDay

            stack.append(curDay)

        return res