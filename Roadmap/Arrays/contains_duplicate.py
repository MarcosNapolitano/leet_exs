class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for i in nums:
            if i not in count:
                count[i]=1
                continue
            count[i]+=1

        if len(count.keys())<len(nums): return True

        return False


solucion = Solution()

print(solucion.containsDuplicate([1,2,3,4,5]))