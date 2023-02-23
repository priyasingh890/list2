import math
class Solution(object):
   def isPowerOfThree(self, n):
      """
      :type n: int
      :rtype: bool
      """
      if not n or n<0:
         return False
      return (math.log10(n)/ math.log10(3)) % 1 == 0
ob1 = Solution()
print(ob1.isPowerOfThree(27))
# print(ob1.isPowerOfThree(15))
# print(ob1.isPowerOfThree(343))