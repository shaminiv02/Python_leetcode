from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        counts = Counter(s)

        for i, c in enumerate(s):
            if counts[c] == 1:
                return i

        return -1