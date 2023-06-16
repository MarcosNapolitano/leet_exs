import random
import math


random.seed(105065465432354352135)
num = random.randrange(3)

random.seed(465445135)

num2 = random.randrange(3)



class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):

        result = []

        for i in strs:

            for j in i:
                result.append((ord(j)*num)*num2)

            result.append((ord(" ")*num)*num2)   

        for i in range(len(result)):
            result[i] = chr(result[i])

        return "".join(result)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, string):

        result = []
        substr = ""

        for i in string:

            i = ord(i)
            i = chr(math.floor((i/num2)/num))

            if i == " ": 
                result.append(substr)
                substr = ""

            else:
                substr+=i

        return result
        # write your code here

a = Solution()

sta = a.encode(["this","is","misuwawe","verdad?"])

print(sta)
print(a.decode(sta))
