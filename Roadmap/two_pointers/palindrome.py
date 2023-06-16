import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'\W',"",s).replace("_","").lower()

        return s[::-1] == s