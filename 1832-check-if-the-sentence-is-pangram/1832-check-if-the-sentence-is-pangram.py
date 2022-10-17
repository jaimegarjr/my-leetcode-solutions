class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Runtime: O(1)
        Space: O(1)
        """
        
        for i in range(ord('a'), ord('z')+1):
            if chr(i) in sentence:
                continue
            else:
                return False
        
        return True