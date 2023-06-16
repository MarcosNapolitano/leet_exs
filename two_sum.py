class Solution:
    def twoSum(self, nums, target):
        
        result_index = []
        data = {}

        for i in range(len(nums)):
            data[nums[i]]=i

        for i in range(len(nums)):
            target2 = target - nums[i] 
            if target2 in data:
                if i!=data[target2]:
                    result_index.append(i)
                    result_index.append(data[target2])
                    return result_index
        

a = Solution()

print(a.twoSum([3,2,4], 6))


