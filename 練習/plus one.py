"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)
        if i == 0:
            return []
        n=0
        for a in range(i-1,-1,-1):
            x = int(digits[a]) + 1
            if x<10:
                digits[a] = x
                n=1
                break
            else:
                digits[a] = 0
    
        if not n :
            digits.insert(0,1)
        return digits
