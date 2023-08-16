class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # temp_array = nums.copy()
        # for i in temp_array:
        #     nums.append(i)
        nums.extend(nums[:]) # I am really proud of this one :)

        return nums


s = Solution()
print(s.getConcatenation([1,2,1]))

