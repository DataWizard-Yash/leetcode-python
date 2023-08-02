class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_value = roman_to_int_mapping[s[i]]

            if i<n-1 and roman_to_int_mapping[s[i+1]] > current_value:
                total -= current_value
            else:
                total += current_value

        return total


s = Solution()
print(s.romanToInt("MCMXCIV")) # Output = 1994

