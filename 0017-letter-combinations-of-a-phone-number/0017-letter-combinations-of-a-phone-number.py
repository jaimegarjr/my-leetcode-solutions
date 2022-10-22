class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numToLetter = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz")
        }
        length = len(digits)
        res = []
        
        def backtrack(digits, comb):
            if not digits:
                res.append("".join(comb))
                return
            
            chars = numToLetter[digits[0]]
            for c in chars:
                comb.append(c)
                backtrack(digits[1:], comb)
                comb.pop()

        backtrack(digits, [])
        return res