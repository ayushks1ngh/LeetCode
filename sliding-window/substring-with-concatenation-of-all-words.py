from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        target = Counter(words)
        ans = []

        for offset in range(word_len):
            left = offset
            curr = Counter()
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    curr[word] += 1
                    count += 1

                    while curr[word] > target[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == total_words:
                        ans.append(left)
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    curr.clear()
                    count = 0
                    left = right + word_len

        return ans