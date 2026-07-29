#--------Time complexity : O(n^2)---------
from typing import List
class Solution:
    def two_sum (self, nums: List[int],target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []

tSum = Solution()
print(tSum.two_sum([2,4,7,9], 9)) 

#--------Time complexity : O(n)-----------
class SolutionSec:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, number in enumerate(nums):
            needed = target - number

            if needed in seen:
                return [seen[needed], i]

            seen[number] = i
        
        return []

tSumSec = SolutionSec()
print(tSumSec.two_sum([3,6,2,1,8,4], 10))