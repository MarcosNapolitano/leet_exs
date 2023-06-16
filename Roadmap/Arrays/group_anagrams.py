class Solution:
    def groupAnagrams(self, strs):


        toCompare = list(map(lambda x: "".join(sorted(x)),strs))
        data = {}
        results = []

        # for i in toCompare:
        #     local = []
        #     if i or i=="":
        #         for j in range(len(toCompare)):
        #             if i==toCompare[j]:
        #                 local.append(strs[j])
        #                 toCompare[j]=None
        #         results.append(local)

        for i in range(len(toCompare)):
            if toCompare[i] not in data:
                data[toCompare[i]]=[strs[i]]
                continue
            data[toCompare[i]].append(strs[i])
            
        for i in data.values():
            results.append(i)


        return sorted(results)


solucion = Solution()

print(solucion.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))