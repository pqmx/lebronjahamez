class CountSquares:

    def __init__(self):
        self.ptsQuantity = {}
        self.pts = set()
        

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) in self.ptsQuantity:
            self.ptsQuantity[(x, y)] += 1
        else:
            self.ptsQuantity[(x, y)] = 1
            self.pts.add((x, y))


    def count(self, point: List[int]) -> int:
        # how do we find a valid square
        res = 0
        px, py = point

        if (px, py) not in pts:
            return 0
        for x, y in self.pts:
            #check if diagonal.
            if x == px or y == py or (px, y) not in self.pts or (x, py) not in self.pts:
                continue
            if abs(x - px) != abs(y - py): 
                continue

            res += (self.ptsQuantity[x, y] * self.ptsQuantity[px, y] *self.ptsQuantity[x, py] *self.ptsQuantity[px, py])
        return res