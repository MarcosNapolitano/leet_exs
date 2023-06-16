class Solution:
    def maxArea(self, height: list[int]) -> int:

        answer = 0

        length = len(height)

        for i in range(length):

            
            point_b = length-1

            while i<point_b:

                current = (height[i] - (height[i] - height[point_b])) * point_b-i

                print(height[i], height[point_b],(point_b-i))
                print(current)
                if current>answer: answer = current

                point_b-=1

        return answer



a = Solution()

print(a.maxArea([1,8,6,2,5,4,8,3,7]))