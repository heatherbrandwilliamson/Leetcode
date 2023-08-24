class Solution:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_gcd = gcd(len(str1), len(str2))
        common_substring = str1[:len_gcd]

        if common_substring * (len(str1) // len_gcd) == str1 and \
            common_substring * (len(str2) // len_gcd) == str2:
            return common_substring
        else:
            return ""

