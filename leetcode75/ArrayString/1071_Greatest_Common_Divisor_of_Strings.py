class Solution(object):
    def divide(self, dividend, divisor):
        counts = len(dividend) / len(divisor)

        # check if it is possible to divide
        if counts != int(counts):
            return False

        # divide
        counts = int(counts)
        for i in range(counts):
            if dividend[i * len(divisor): (i + 1) * len(divisor)] != divisor:
                return False

        return True

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result_index = -1
        for i in range(min(len(str1), len(str2))):
            # check if str1[:i+1] can divide both
            if str1[i] == str2[i]:
                if self.divide(str1, str1[:i + 1]) and self.divide(str2, str2[:i + 1]):
                    result_index = i
            else:
                break
        return str1[:result_index + 1]

    def good_gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])


str1 = ["ABCABC", "ABABAB", "ABABABAB", "LEET", "A"]
str2 = ["ABC", "ABAB", "ABAB", "CODE", "A"]
for s1, s2 in zip(str1, str2):
    result = Solution().gcdOfStrings(s1, s2)
    print(s1, s2, result)