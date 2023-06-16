import collections

class Solution:
    def topKFrequent(self, nums, target):

        # data = {}
        # result = []

        # for i in nums:
        #     if i not in data:
        #         data[i] = 1
        #         continue
        #     data[i]+=1


        # while(target):
        #     key = max(data, key = lambda x: data[x])
        #     result.append(key)
        #     del data[key]
        #     target-=1

        data = collections.Counter(nums)
        result = []
        
        for i in data.most_common(target): result.append(i[0])

            
        return result


solucion = Solution()

print(solucion.topKFrequent([1,1,1,2,2,3],2))