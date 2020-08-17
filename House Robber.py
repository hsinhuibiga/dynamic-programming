#House Robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        N = len(nums)
        dp = [0] * (N + 1)
        dp[1] = nums[0]
        for i in range(1, N):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[-1]