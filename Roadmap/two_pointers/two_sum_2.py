class Solution:
    def twoSum(self, numbers, target):

        length = len(numbers)

        answer = []

        for i in numbers:

            found = True

            j = length-1

            while i + numbers[j] != target:
                j-=1
                if numbers[j]==i:
                    found = False
                    break
                found = False


            if found: answer=[numbers.index(i), numbers.index(j)]






a = Solution

print(a.twoSum([2,7,11,15], 9))