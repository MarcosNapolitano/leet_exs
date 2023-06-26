class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

    	objective = []

    	for i in matrix:
    		if i[0]<=target<=i[-1]:
    			objective = i

    	if not objective:
    		return False	

    	high = len(objective)-1

    	def recursive(arr, target, low=0, high=high):

            mid_point = low+(high-low)//2

            if objective[high]==target:
                return True
            if objective[low] == target:
                return True
            if objective[mid_point]==target:
                return True

            if high == low+1 or high == low: 
                return False


            if objective[mid_point]>target:
                return recursive(objective, target, high = mid_point-1,low=0)
            else:
                return recursive(objective, target, low = mid_point+1, high=high)

    	return recursive(objective, target)



a = Solution()
print(a.searchMatrix([[1]],1))