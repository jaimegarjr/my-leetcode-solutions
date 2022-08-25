class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Runtime: O(v+e)
        # Space: O(v+e)
        visited = set()
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
            
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for p in preMap[crs]:
                if not dfs(p): return False
            
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True