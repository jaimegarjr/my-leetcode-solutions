class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Gets all the keypad letter combinations of a given num string 
        Runtime: O(4^n * n)
        Space: O(n)
        """
        res = []
        numToLetter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(digits, comb):
            if not digits:
                res.append("".join(comb))
                return

            chars = numToLetter[digits[0]]
            for c in chars:
                comb.append(c)
                backtrack(digits[1:], comb)
                comb.pop()

        if digits:
            backtrack(digits, [])
        return res