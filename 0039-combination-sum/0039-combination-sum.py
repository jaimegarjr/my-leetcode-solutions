class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(candidates, comb, total):
            if not candidates or total > target:
                return
            if total == target:
                res.append(comb[:])
                return

            comb.append(candidates[0])
            backtrack(candidates, comb, total + candidates[0])
            comb.pop()
            backtrack(candidates[1:], comb, total)

        backtrack(candidates, [], 0)
        return res