class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        lrcd = defaultdict(int)
        rrcd = Counter(nums)

        n = len(nums)
        for i in range(n):
            lrcd[nums[i]] += 1
            rrcd[nums[i]] -= 1
            ll = i + 1
            rl = n - i - 1
            if (
                lrcd[nums[i]] > ll // 2 and
                rrcd[nums[i]] > rl // 2
            ):
                return i
        
        return -1