#-----------------Time complexity O(n)---------------
class Solution:
    def isPalindrome(self, x:int)-> bool:
        return str(x) == str(x)[::-1]
solution = Solution()
print (solution.isPalindrome(121))
print (solution.isPalindrome(-121))
print (solution.isPalindrome(232))
print (solution.isPalindrome(789))

#-------------Time complexity O(n) but with reversing the number not changing it to string----------
class SolutionSec:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        return original == reverse
solution = SolutionSec()
print (solution.isPalindrome(121))
print (solution.isPalindrome(-121))
print (solution.isPalindrome(232))
print (solution.isPalindrome(789))