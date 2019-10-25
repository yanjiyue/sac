#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321
#Example 2:

#Input: -123
#Output: -321
#Example 3:

#Input: 120
#Output: 21
#Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        if x<-(2**31) or x>(2**31-1) :
            return 0
        result=0
        y=abs(x)
        while y:
            result=result*10+y%10
            y=y//10
            
        if result<-(2**31) or result>(2**31-1) :
            return 0
        
        elif x<0:return -(result)
        
        else:return result
