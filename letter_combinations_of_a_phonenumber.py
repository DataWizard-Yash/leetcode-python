class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        number_to_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "xyz"
        }

        char_list = [number_to_letter_map[d] for d in digits]
        if len(digits) == 0:
            return []
        from itertools import product
        result = [''.join(combination) for combination in product(*char_list)]
        return result




s = Solution()
print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
