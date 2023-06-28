from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def recursive(piles, h, low=1, high=max(piles)):

            k = (low + high)//2

            if low > high:
                #a lo sumo tarda una hora mas si es un valor decimal
                return k+1

            hours = 0

            for j in piles:
                hours+=ceil(j/k)

            if hours<=h:
                return recursive(piles, h, high = k-1, low=1)
            else:
                return recursive(piles, h, low = k+1, high=high)

        return recursive(piles, h)

        


a = Solution()

print(a.minEatingSpeed([1,1,1,999999999], 10))


