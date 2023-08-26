class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            if s == s[::-1]:
                return True
        else:
            # Logic to find all substrings of "s"
            pass


s = Solution()
print(s.longestPalindrome("abc"))