class Solution:

    def dailyTemperatures(self, arr):

        stack = []

        answer = [0] * len(arr)

        for i, j in enumerate(arr):

            while stack and j > stack[-1][0]:
                s_temp, s_ind = stack.pop()
                answer[s_ind] = (i-s_ind)
            stack.append([j,i])

        return answer


temperatures = [73,74,75,71,69,72,76,73]



a = Solution()

print(a.dailyTemperatures(temperatures))
