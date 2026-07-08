class Solution(object):
    def printVertically(self, s):
        words = s.split()
        max_len = max(len(word) for word in words)

        answer = []

        for i in range(max_len):
            vertical = ""

            for word in words:
                if i < len(word):
                    vertical += word[i]
                else:
                    vertical += " "

            answer.append(vertical.rstrip())

        return answer
        