class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 1:
            return list(phone[digits[0]])

        result = []

        for a in phone[digits[0]]:
            for b in phone[digits[1]]:
                result.append(a + b)

        return result