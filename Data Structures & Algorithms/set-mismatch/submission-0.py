class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vis = [False for _ in range(n)]
        ret = []

        for num in nums:
            if vis[num - 1] == True:
                ret.append(num)
            vis[num - 1] = True
        
        for i in range(n):
            if vis[i] == False:
                ret.append(i + 1)
        
        return ret

