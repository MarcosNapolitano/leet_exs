class Solution:
    def findMin(self, nums: list[int]) -> int: 

        length = len(nums)-1

        res = None

        if nums[0]>nums[-1]:

            #was rotated
            l, r = 0, length

            if length<=2:
                return min(nums[l],nums[l+1], nums[r])
            
            while l<r: 

                mid_point = (r-l)//2

                if not mid_point:
                    l+=1

                temp = nums[l:r+1]

                print(temp, mid_point, l, r)

                if not res:
                    res = temp[mid_point] 
                elif temp[mid_point]< res:
                    res = temp[mid_point]

                if temp[mid_point]>=temp[0]:
                    l += mid_point


                else: r -= mid_point

            return res

        else:
            #is ordered
            return nums[0]


a = Solution()

#depende de si el principio o el final es menor, ahi es donde buscamos

print(a.findMin([5,6,7,8,9,1,2,3,4]))