class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        common_prefix = ""
        for char_group in zip(*strs):
            if len(set(char_group)) == 1:
                common_prefix += char_group[0]
            else:
                break

        return common_prefix

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
