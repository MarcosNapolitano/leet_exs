class Solution:

    def lengthOfLongestSubstring(self, s: str):
        substrings = []
        candidates = []
        maxLength = 0

        for i in range(len(s)):
            if i==0:
                continue
            for j in range(len(s)):
                if s[j:i] in substrings:
                    continue
                substrings.append(s[j:i])
                substrings.append(s[i:])

        for i in substrings:
            for j in range(len(i)):
                current = {}
                if current[i] not in current: current[i] = 1
                else: current[i[j]] += 1

            
        

        return current





solucion = Solution()

print(solucion.lengthOfLongestSubstring("dvdf"))