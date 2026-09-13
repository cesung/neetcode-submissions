class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        postfix = [1]
        for num in nums[::-1]:
            postfix.append(postfix[-1] * num)
        postfix = postfix[::-1]

        n = len(nums)
        res = [
            prefix[i]*postfix[i+1]
            for i in range(n)
        ]

        return res