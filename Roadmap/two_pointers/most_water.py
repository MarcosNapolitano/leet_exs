class Solution:
    def maxArea(self, height: list[int]) -> int:

        answer = 0
        point_a = 0
        point_b = len(height)-1

        while point_a<point_b:

            answer = max(answer, min(height[point_a], height[point_b]) * (point_b - point_a))

            if height[point_a]<=height[point_b]:  
                point_a+=1
            else:
                point_b-=1

        return answer



a = Solution()

lol = [1,8,6,2,5,4,8,3,7]


print(a.maxArea(horriblylarge))

