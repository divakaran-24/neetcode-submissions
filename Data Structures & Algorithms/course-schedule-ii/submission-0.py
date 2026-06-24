class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visited,cycle = set(),set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
                
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) ==  False:
                return []
        return output

    


        