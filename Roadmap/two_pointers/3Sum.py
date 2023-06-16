class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        answer = []
        index = {}

        length = len(nums)

        for i,j in enumerate(nums):

            if i>0 and j == nums[i-1]:
                continue

            point_a = i+1
            point_b = length-1

            if point_a == point_b:
                break

            
            while point_a < point_b:

                total = j + nums[point_a] + nums[point_b]


                if total > 0:
                    point_b-=1
                    
                if total < 0:
                    point_a+=1

                if point_a == point_b:
                    break

                if total == 0:

                    current_sol = [j, nums[point_a], nums[point_b]]

                    try:
                        index[str(current_sol)]+=1
                        curr_index = index[str(current_sol)]

                    except:
                        curr_index = index.setdefault(str(current_sol), 1)
                    
                    if curr_index==1:

                    answer.append(current_sol)
                    point_a+=1
      
                
        return answer



a = Solution()

print(a.threeSum([-1,0,1,2,-1,-4]))