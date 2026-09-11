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
            
           
            cycle.add(crs)
            
            
            if crs in graph:
                for c in graph[crs]:
                    if cycleExists(c):
                        return True
            
            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            
            return False
        


        for i in range(numCourses):
            if i not in graph:
                output.append(i)
                continue
            if cycleExists(i):
                return []
        return output
        


        for i in allCourses:
            if cycleExists(i):
                return []
        return sorted(output)
            
        

        


    



        
    