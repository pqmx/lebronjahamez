class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph= {n : set() for n in range(numCourses)}
        
        for main, pre in prerequisites:
            graph[pre].add(main)
        
        def cycleExists(crs, visited):
            if crs in visited:
                return True

            if len(graph[crs]) == 0:
                return False

            visited.add(crs)


            for pre in graph[crs]:
                if cycleExists(pre, visited):
                    return True
            visited.remove(crs)
            graph[crs] = set()

            return False

        for n in range(numCourses):
            if cycleExists(n, set()):
                return False
        return True