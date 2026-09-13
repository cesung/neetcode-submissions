class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        
        self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""

        tvalues = self.tmap[key]
        left, right = 0, len(tvalues) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if tvalues[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid
        
        if tvalues[left][1] > timestamp:
            return ""
        
        return tvalues[left][0]
