class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist_sqr(x, y):
            return x**2 + y**2

        def quickSelect(l, r):
            pivot, ptr = points[r], l
            for i in range(l, r):
                if points[i][1] <= pivot[1]:
                    points[i], points[ptr] = points[ptr], points[i]
                    ptr += 1
            
            points[ptr], points[r] = points[r], points[ptr]

            if ptr > k:
                return quickSelect(l, ptr - 1)
            if ptr < k:
                return quickSelect(ptr + 1, r)
            
            return [p for p, dist in points[:ptr + 1]]
        
        points = [
            [[x,y], dist_sqr(x, y)]
            for (x, y) in points
        ]
        n = len(points)
        k = k - 1

        return quickSelect(0, n - 1)


