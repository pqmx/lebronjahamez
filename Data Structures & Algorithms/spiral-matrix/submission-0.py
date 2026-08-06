class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        down, right, up, left = dir
        visited_list = []
        start = (0, 0)

        curDir = right
        while len(visited) < len(matrix) * len(matrix[0]):
            r, c = start
            visited.add((r, c))
            visited_list.append(matrix[r][c])

            nr, nc = curDir # dir

            tr, tc = nr + r, nc + c # projected

            if 0 <= tr < len(matrix) and 0 <= tc < len(matrix[0]) and (tr, tc) not in visited:
                start = (tr, tc)
            else:
                if curDir == right:
                    curDir = down
                elif curDir == down:
                    curDir = left
                elif curDir == left:
                    curDir = up
                else:
                    curDir = right
                

                ar, ac = curDir
                start = (r + ar, c + ac)
        
        return visited_list
            
           
        


