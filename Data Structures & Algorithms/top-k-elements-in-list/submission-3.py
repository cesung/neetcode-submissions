class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        cntr = {}
        for num in nums:
            cntr[num] = 1 + cntr.get(num, 0)
        
        buckets = [[] for _ in range(n + 1)]
        for val, cnt in cntr.items():
            buckets[cnt].append(val)
        
        res = []
        while k and n:
            if buckets[n]:
                res.extend(buckets[n])
                k -= len(buckets[n])
            n -= 1
        
        return res

