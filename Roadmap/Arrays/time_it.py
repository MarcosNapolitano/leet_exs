import timeit
from longest_consecutive_sequence import Solution, nums

testcode = '''

a = Solution()

a.longest_consecutive(nums)

'''

print(timeit.timeit(stmt=testcode, setup="from longest_consecutive_sequence import Solution, nums",number=100))


