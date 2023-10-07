class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        has_duplicate = False

        for num in nums:
            if num in num_set:
                has_duplicate = True
                break
            else:
                num_set.add(num)

        return has_duplicate


s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
