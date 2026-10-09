class CountSquares:

    def __init__(self):
        self.p_cntr = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.p_cntr[tuple(point)] += 1
        
    def count(self, px: List[int]) -> int:
        px = tuple(px)
        cnt = 0
        for py in self.p_cntr.keys():
            if (
                px == py or
                px[0] == py[0] or
                px[1] == py[1]
            ):
                continue
                
            pa, pb = (px[0], py[1]), (py[0], px[1])
            if (
                pa in self.p_cntr and
                pb in self.p_cntr
            ):
                print(px, py, pa, pb)
                cnt += (
                    self.p_cntr[pa] *
                    self.p_cntr[pb] *
                    self.p_cntr[py]
                )
        
        return cnt
                

