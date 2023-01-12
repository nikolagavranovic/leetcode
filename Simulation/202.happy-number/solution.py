# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# * Starting with any positive integer, replace the number by the sum of the squares of its digits.
# * Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# * Those numbers for which this process ends in 1 are happy.
# * Return true if n is a happy number, and false if not

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        results = []
        while n != 1:
            digits = self.getDigits(n)
            n = 0
            for d in digits:
                n += d ** 2
            
            if n in results:
                return False
            else:
                results.append(n)
        
        return True
            

    def getDigits(self, n):
        retVal = []
        while n > 0:
            retVal.insert(0, n % 10)
            n //= 10
        return retVal
