from functools import reduce

class Solution:
    def productExceptSelf(self, nums):

        # result = []
        # maxim = reduce(lambda x,y:x*y,nums)

        # for i in range(len(nums)):

        #     if nums[i]==1: 
        #         result.append(maxim) 
        #         continue
        #     if nums[i]==-1: 
        #         result.append(0-maxim) 
        #         continue

        #     remove = nums[i]

        #     del nums[i]

        #     result.append(reduce(lambda x,y:x*y,nums))

        #     nums.insert(i,remove)

        return result

solucion = Solution()

print(solucion.productExceptSelf([1,2,3,4]))