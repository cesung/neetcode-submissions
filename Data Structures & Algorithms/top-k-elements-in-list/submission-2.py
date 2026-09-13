class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cntr = {}
        # 1-index
        bucket = {i: set() for i in range(n + 2)}
        max_freq = 0

        for num in nums:
            if num not in cntr:
                cntr[num] = 1
                bucket[1].add(num)
            bucket[cntr[num]].remove(num)
            cntr[num] += 1
            bucket[cntr[num]].add(num)
            max_freq = max(
                max_freq,
                cntr[num]
            )
        
        res = []
        while k and max_freq:
            if bucket[max_freq]:
                res.extend(bucket[max_freq])
                k -= len(bucket[max_freq])
            max_freq -= 1
        
        return res
