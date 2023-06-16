class Solution:
    
    def findMedianSortedArrays(self, nums1: int, nums2: int):

        def join(arr1, arr2):

            merged = []
            for i in range(len(arr1)):
                if arr1[i] < arr2[i]:
                    merged.append(arr1[i])
                else:
                    merged.append(arr2[i])
            
            return merged
        
        def divide(arr):

            if len(arr)==1:
                return arr

            side1 = arr[:len(arr)//2]
            side2 = arr[len(arr)//2:]

            return join(divide(side1),divide(side2))


solucion = Solution()

print(solucion.findMedianSortedArrays([1,2], [3,4]))