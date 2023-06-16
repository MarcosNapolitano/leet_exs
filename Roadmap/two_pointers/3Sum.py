class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        answer = []
        answer2 = {}

        length = len(nums)

        for i in range(len(nums)):

            point_a = i+1
            point_b = length-1

            if point_a == point_b:
                break

            
            while point_a < point_b:

                total = nums[i] + nums[point_a] + nums[point_b]


                if total > 0:
                    point_b-=1
                    
                if total < 0:
                    point_a+=1

                if point_a == point_b:
                    break

                if total == 0:

                    try:

                    index = answer2.setdefault(str([nums[i], nums[point_a], nums[point_b]]), 1)
                    
                    if index==1:

                        answer.append([nums[i], nums[point_a], nums[point_b]])
                    point_a+=1
      
                
        return answer



a = {"[3]":1}

a["2"] +=1
a["2"] += 5


print(a)