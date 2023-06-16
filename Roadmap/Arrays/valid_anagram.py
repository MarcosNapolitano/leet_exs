class Solution:
    def isAnagram(self, str1, str2):
        return sorted(str1)==sorted(str2)

solucion = Solution()

print(solucion.isAnagram("holaa", "holaa"))