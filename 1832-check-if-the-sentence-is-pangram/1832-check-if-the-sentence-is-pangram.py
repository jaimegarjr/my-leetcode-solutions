class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Runtime: O(n)
        Space: O(1) at most 26
        """
        return len(set(sentence)) == 26