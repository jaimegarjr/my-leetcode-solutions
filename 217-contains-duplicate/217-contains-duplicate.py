class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Plan:
        1. iterate linearly
        2. store into a hash
        3. if a num is ever in the map again, True
        
        Runtime: O(n)
        Space: O(n)
        """
        num_map = {}
        
        for n in nums:
            if n in num_map:
                return True
            else:
                num_map[n] = 1
                
        return False