class Solution:
    def search(self, nums: list[int], target: int) -> int:

        length = len(nums)-1

        l, r = 0, length

        while l<=r: 

            mid_point = (r-l)//2

            print(nums[l:r+1], mid_point)

            if nums[l] == target: return l
            if nums[r] == target: return r

            if not mid_point:
                break

            if nums[l+mid_point] == target: return mid_point+l

            if nums[0]>nums[-1]:

                #was rotated

                #falta terminar el criterio aca nomas
                if nums[l+mid_point]>nums[l]:
                    if nums[l]<target<nums[l+mid_point]:
                        r -= mid_point
                    else:
                        l += mid_point
                else: 
                    if nums[r]> target > nums[l+mid_point]:
                        l += mid_point
                    else:
                        r -= mid_point

            else:
                #is ordered
                if nums[l+mid_point]<target:
                    l += mid_point

                else: r -= mid_point

        return -1

a = Solution()

print(a.search([8,1,2,3,4,5,6,7],10))

arr2 =  [4,5,6,7,0,1,2]