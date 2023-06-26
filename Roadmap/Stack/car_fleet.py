class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        fleets = []
        time_to_arrive = []
        stack = []

        ans = 0

        for i in range(len(position)):
            fleets.append((position[i], speed[i]))

        fleets.sort()

        for i in fleets:
            time_to_arrive.append((target-i[0]) / i[1])

        for i in range(len(time_to_arrive)):

            if not stack:
                stack.append(time_to_arrive[i])
                ans+=1
                continue

            if stack:
                if time_to_arrive[i]<stack[-1]:

                    stack = []       
                    stack.append(time_to_arrive[i])
                    ans += 1
                    continue

                if time_to_arrive[i]>=stack[-1]:
                    while stack:
                        stack.pop()
                        ans-=1
                    stack.append(time_to_arrive[i])



        return ans, time_to_arrive, fleets


a = Solution()

print(a.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
