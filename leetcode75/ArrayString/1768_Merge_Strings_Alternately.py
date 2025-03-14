class Solution(object):
    def bad_MergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) > len(word2):
            long, short = word1, word2
        else:
            long, short = word2, word1

        total_length = len(long) + len(short)
        result = ["0"] * total_length
        result[-len(long):] = long

        for i in range(total_length):
            q, r = divmod(i, 2)
            if r == 0 and q < len(word1):
                result[i] = word1[q]
            elif r == 1 and q < len(word2):
                result[i] = word2[q]
            else:
                break

        return "".join(result)

    def good_MergeAlternately(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        result = ""
        for i in range(len1 + len2):
            if i < len1:
                result += word1[i]
            if i < len2:
                result += word2[i]
        return result


word1 = "abc"
word2 = "123456"

res = Solution().good_MergeAlternately(word1, word2)
print(res)
