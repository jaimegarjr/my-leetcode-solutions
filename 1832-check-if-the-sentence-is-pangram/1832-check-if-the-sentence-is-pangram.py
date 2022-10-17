class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Runtime: O(n)
        Space: O(1)
        """
        
        for i in range(ord('a'), ord('z')+1):
            if chr(i) in sentence: # O(n)
                continue
            else:
                return False
        
        return True