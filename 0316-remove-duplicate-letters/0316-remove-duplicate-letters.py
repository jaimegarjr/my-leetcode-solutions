class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        latestOccurence = {}
        
        for i, c in enumerate(s):
            latestOccurence[c] = i 
        
        
        for i, c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] > c and latestOccurence[stack[-1]] > i:
                    prevC = stack.pop()
                    visited.remove(prevC)
                
                stack.append(c)
                visited.add(c)
            
        return "".join(stack)
        