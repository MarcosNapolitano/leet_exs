class Solution:
    def twoSum(self, numbers, target):

        answer = []
        point_a = 0
        point_b = len(numbers)-1
        total = numbers[point_a] + numbers[point_b]

        while total != target:
        
            if total > target:
                point_b-=1
                
            if total < target:
                point_a+=1

            total = numbers[point_a] + numbers[point_b]
               
        answer = [point_a+1, point_b+1]
                
        return answer


a = Solution()

print(a.twoSum([2,7,11,15], 9))




