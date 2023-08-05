class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        seconds = 0

        while max_num > min(nums):
            new_max = max_num
            for i in range(len(nums)):
                if nums[i] == max_num:
                    new_max = max(new_max, (nums[i] + 1) // 2)
                else:
                    new_max = max(new_max, nums[i])

            for i in range(len(nums)):
                nums[i] = new_max - (max_num - nums[i])

            max_num = new_max
            seconds += 1

        return seconds

# Test case
s = Solution()
print(s.minimumSeconds([8, 13, 3, 3]))  # Output: 1
