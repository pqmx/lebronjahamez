class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {}
        allCourses = set()
        for crs, pre in prerequisites:
            if pre not in graph:
                graph[pre] = []
            graph[pre].append(crs)
            allCourses.add(crs)
            allCourses.add(pre)
    

        cycle, visit = set(), set()
        output = []
        def cycleExists(crs):
            if crs in cycle:
                return True
            if crs in visit:
                return False
            
            visit.add(crs)
            cycle.add(crs)
            output.append(crs)
            
            if crs not in graph:
                return False
            for c in graph[crs]:
                if cycleExists(c):
                    return True
            

            
            return False
        


        for i in range(numCourses):
            if i not in graph:
                output.append(i)
                continue
            if cycleExists(i):
                return []
        return output
        


        for i in allCourses:
            cycle = set()
            if i not in graph:
                output.append(i)
                continue
            if cycleExists(i):
                return []
        return output
            
        

        


    



        
    