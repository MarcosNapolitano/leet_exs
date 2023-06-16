class Solution:
    def longestCommonPrefix(self, strs):

        result = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return result
            result = result + strs[0][i]
        return result



solucion = Solution()

print(solucion.longestCommonPrefix(["flight","flower","flow","cat"]))