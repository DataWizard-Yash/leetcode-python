class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))

        x_rev = int(x_str[::-1]) * (-1 if x < 0 else 1)

        return x_rev


s = Solution()
print(s.reverse(123))