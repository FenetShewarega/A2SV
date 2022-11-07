class Solution(object):
    def longestSubarray(self, nums, limit):
        max_d = deque()
        min_d = deque()
        i = 0
        res = 0

        for j,n in enumerate(nums):
            while max_d and n > max_d[-1]:
                max_d.pop()
            max_d.append(n)

            while min_d and n < min_d[-1]:
                min_d.pop()
            min_d.append(n)

            while max_d[0] - min_d[0] > limit:
                if max_d[0] == nums[i]:
                    max_d.popleft()
                if min_d[0] == nums[i]:
                    min_d.popleft()
                i += 1
            res = max(res,(j-i+1))            

        return res
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        